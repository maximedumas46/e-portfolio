#!/usr/bin/env python3
"""
Copy every file the site still loads from Wix into this repository.

- Images  (front matter / _config.yml entries with a Wix `id:`) -> assets/media/<id>-<width>.webp
          in the widths used by _includes/image.html (480, 960 and min(original, 1600))
- CVs     (_config.yml `cv:` urls on filesusr.com / usrfiles.com) -> assets/cv/*.pdf
- Videos  (front matter `video:` urls on video.wixstatic.com)      -> assets/video/*.mp4

Then it switches the site to the local copies (`media_local: true` in _config.yml and the
CV / video urls rewritten). Everything is downloaded first: if any download fails, nothing
in the repository is changed.

Run by .github/workflows/import-wix-media.yml (Actions tab -> "Import Wix media" -> Run workflow).
Requires: Python 3.9+, PyYAML.
"""
import os
import re
import shutil
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "_config.yml"
MAX_WIDTH = 1600
SMALL_WIDTHS = (480, 960)  # must match _includes/image.html
WIX_ID = re.compile(r"^[0-9a-f]{6}_[0-9a-f]{32}~mv2\.[A-Za-z0-9]+$")
SKIP_DIRS = {".git", "_site", ".jekyll-cache", "assets", "vendor", "node_modules", "scripts", ".github"}
FAKE = os.environ.get("WIX_IMPORT_FAKE") == "1"  # local testing only: no network

FAKE_BYTES = {
    "image/webp": b"RIFF\x00\x00\x00\x00WEBPVP8 ",
    "application/pdf": b"%PDF-1.4\n%fake\n",
    "video/mp4": b"\x00\x00\x00\x18ftypmp42",
}
MAGIC = {
    "image/webp": lambda b: b[:4] == b"RIFF" and b[8:12] == b"WEBP",
    "application/pdf": lambda b: b[:5] == b"%PDF-",
    "video/mp4": lambda b: b[4:8] == b"ftyp",
}


def log(msg):
    print(msg, flush=True)


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if path.name == "_config.yml":
        return text, yaml.safe_load(text) or {}
    if not text.startswith("---"):
        return text, None
    end = text.find("\n---", 3)
    if end == -1:
        return text, None
    return text, yaml.safe_load(text[3:end]) or {}


def walk(node, found_images, found_videos):
    if isinstance(node, dict):
        img_id = node.get("id")
        if isinstance(img_id, str) and WIX_ID.match(img_id) and node.get("width") and node.get("height"):
            found_images[img_id] = (int(node["width"]), int(node["height"]))
        video = node.get("video")
        if isinstance(video, str) and "video.wixstatic.com" in video:
            found_videos.add(video)
        for v in node.values():
            walk(v, found_images, found_videos)
    elif isinstance(node, list):
        for v in node:
            walk(v, found_images, found_videos)


def site_files():
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if path.is_file() and not (set(rel.parts[:-1]) & SKIP_DIRS) and path.suffix in {".md", ".html", ".yml"}:
            if path.suffix == ".yml" and path != CONFIG:
                continue
            yield path


def image_widths(width):
    full = min(width, MAX_WIDTH)
    return [w for w in SMALL_WIDTHS if w < full] + [full]


def download(url, dest, expected_type):
    if FAKE:
        dest.write_bytes(FAKE_BYTES[expected_type])
        return
    last_error = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (portfolio media import)"})
            with urllib.request.urlopen(req, timeout=120) as resp, open(dest, "wb") as out:
                shutil.copyfileobj(resp, out)
            head = dest.read_bytes()[:16]
            if not MAGIC[expected_type](head):
                raise ValueError(f"unexpected content (not {expected_type})")
            return
        except Exception as exc:  # noqa: BLE001 - retried, then reported
            last_error = exc
            time.sleep(2 ** attempt)
    raise RuntimeError(f"{url}: {last_error}")


def main():
    images, videos, files_text = {}, set(), {}
    for path in site_files():
        text, data = front_matter(path)
        files_text[path] = text
        if data:
            walk(data, images, videos)

    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}
    cvs = [c for c in config.get("cv", []) if re.search(r"(filesusr|usrfiles)\.com/.+\.pdf", str(c.get("url", "")))]

    log(f"Found {len(images)} images, {len(cvs)} CVs, {len(videos)} videos on Wix.")

    plan = []  # (url, final path, content type)
    for img_id, (width, height) in sorted(images.items()):
        base = img_id.split("~")[0]
        for w in image_widths(width):
            h = height * w // width
            url = f"https://static.wixstatic.com/media/{img_id}/v1/fit/w_{w},h_{h},q_85/{base}.webp"
            final = ROOT / "assets" / "media" / f"{base}-{w}.webp"
            if not final.exists():  # already imported by a previous run
                plan.append((url, final, "image/webp"))

    url_rewrites = {}
    for cv in cvs:
        label = str(cv.get("label", "CV")).upper()
        suffix = label.split("_", 1)[1] if "_" in label else label
        local = f"/assets/cv/CV_DUMAS_MAXIME_{suffix}.pdf"
        plan.append((cv["url"], ROOT / local.lstrip("/"), "application/pdf"))
        url_rewrites[cv["url"]] = local

    for i, video in enumerate(sorted(videos), start=1):
        name = "pitch-elevator.mp4" if len(videos) == 1 else f"video-{i}.mp4"
        local = f"/assets/video/{name}"
        plan.append((video, ROOT / local.lstrip("/"), "video/mp4"))
        url_rewrites[video] = local

    log(f"{len(plan)} files to download.")

    # 1. Download everything to a temporary folder first
    tmp = Path(tempfile.mkdtemp(prefix="wix-media-"))
    staged = []
    try:
        for n, (url, final, ctype) in enumerate(plan, start=1):
            target = tmp / f"{n:04d}"
            log(f"[{n}/{len(plan)}] {final.relative_to(ROOT)}")
            download(url, target, ctype)
            staged.append((target, final))
    except Exception as exc:  # noqa: BLE001
        log(f"\nERROR: {exc}\nNo file of the site was changed.")
        shutil.rmtree(tmp, ignore_errors=True)
        return 1

    # 2. Move the files into the repository
    total = 0
    for target, final in staged:
        final.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(target), final)
        total += final.stat().st_size
        if final.stat().st_size > 50 * 1024 * 1024:
            log(f"WARNING: {final.relative_to(ROOT)} is larger than 50 MB.")
    shutil.rmtree(tmp, ignore_errors=True)

    # 3. Point the site at the local copies
    for path, text in files_text.items():
        new = text
        for old_url, local in url_rewrites.items():
            new = new.replace(old_url, local)
        if path == CONFIG:
            new, count = re.subn(r"(?m)^media_local:\s*false\s*$", "media_local: true", new)
            if count == 0 and not re.search(r"(?m)^media_local:\s*true\s*$", new):
                new = new.rstrip("\n") + "\n\nmedia_local: true\n"
        if new != text:
            path.write_text(new, encoding="utf-8")
            log(f"Updated {path.relative_to(ROOT)}")

    log(f"\nDone: {len(staged)} files ({total / 1024 / 1024:.1f} MB) copied into the repository.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
