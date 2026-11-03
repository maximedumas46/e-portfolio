// Mobile menu
(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (!toggle || !nav) return;

  function setOpen(open) {
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    nav.classList.toggle("is-open", open);
  }

  toggle.addEventListener("click", function () {
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && nav.classList.contains("is-open")) {
      setOpen(false);
      toggle.focus();
    }
  });
})();

// Contact form: opens the visitor's e-mail app with the message pre-filled.
(function () {
  var form = document.getElementById("contact-form");
  if (!form) return;

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var f = form.elements;
    var name = (f.firstname.value + " " + f.lastname.value).trim();
    var body = f.message.value + "\n\n— " + name + " (" + f.email.value + ")";
    var href = "mailto:" + form.getAttribute("data-email") +
      "?subject=" + encodeURIComponent(f.object.value) +
      "&body=" + encodeURIComponent(body);
    window.location.href = href;
  });
})();

// Lightbox for images (progressive enhancement: links open the image without JS).
(function () {
  var dialog = document.querySelector(".lightbox");
  if (!dialog || typeof dialog.showModal !== "function") return;

  var links = Array.prototype.slice.call(document.querySelectorAll("a[data-lightbox]"));
  if (!links.length) return;

  var img = dialog.querySelector("img");
  var caption = dialog.querySelector("figcaption");
  var group = [];
  var current = 0;

  function show(i) {
    current = (i + group.length) % group.length;
    var link = group[current];
    img.src = link.getAttribute("href");
    img.alt = link.getAttribute("data-caption") || "";
    caption.textContent = link.getAttribute("data-caption") || "";
  }

  links.forEach(function (link) {
    link.addEventListener("click", function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault();
      var name = link.getAttribute("data-lightbox");
      group = links.filter(function (l) { return l.getAttribute("data-lightbox") === name; });
      if (group.length < 2) dialog.setAttribute("data-single", "");
      else dialog.removeAttribute("data-single");
      show(group.indexOf(link));
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
