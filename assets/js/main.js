// Lightbox for project images (progressive enhancement: links open the image without JS).
(function () {
  var dialog = document.querySelector(".lightbox");
  if (!dialog || typeof dialog.showModal !== "function") return;

  var links = Array.prototype.slice.call(document.querySelectorAll("a[data-lightbox]"));
  if (!links.length) return;

  var img = dialog.querySelector("img");
  var caption = dialog.querySelector("figcaption");
  var current = 0;

  function show(i) {
    current = (i + links.length) % links.length;
    var link = links[current];
    img.src = link.getAttribute("href");
    img.alt = link.getAttribute("data-caption") || "";
    caption.textContent = link.getAttribute("data-caption") || "";
  }

  if (links.length < 2) dialog.setAttribute("data-single", "");

  links.forEach(function (link, i) {
    link.addEventListener("click", function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault();
      show(i);
      dialog.showModal();
    });
  });

  dialog.querySelector(".lightbox-close").addEventListener("click", function () { dialog.close(); });
  dialog.querySelector(".lightbox-prev").addEventListener("click", function () { show(current - 1); });
  dialog.querySelector(".lightbox-next").addEventListener("click", function () { show(current + 1); });

  // Close when clicking outside the image
  dialog.addEventListener("click", function (e) {
    if (e.target === dialog || e.target.tagName === "FIGURE") dialog.close();
  });

  dialog.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") show(current - 1);
    if (e.key === "ArrowRight") show(current + 1);
  });

  dialog.addEventListener("close", function () { img.removeAttribute("src"); });
})();
