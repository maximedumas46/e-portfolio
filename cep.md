---
layout: page
title: CEP
heading: Career Evolution Plan
permalink: /cep/
eyebrow: "CAM · M1 FISA · Semester 7"
intro: "My Career Evolution Plan for the jury of Tuesday 1 December 2026: my poster, the five slides of my presentation in English, my CVs and LinkedIn profile, and my mobility application in French and English."
poster:
  src: /assets/cep/poster-cep.webp
  width: 2000
  height: 1125
  alt: "Career Evolution Plan poster: timeline 2022–2031 and plans A, B and C"
  title: "My Career Evolution Plan 2022–2031"
slides:
  - { src: /assets/cep/slide-1.webp, width: 1600, height: 900, title: "1 · Company one-pager: SAS Santerne Toulouse in the VINCI group" }
  - { src: /assets/cep/slide-2.webp, width: 1600, height: 900, title: "2 · Economic figures 1: wealth creation and key ratios" }
  - { src: /assets/cep/slide-3.webp, width: 1600, height: 900, title: "3 · Economic figures 2: capital, financing and cash" }
  - { src: /assets/cep/slide-4.webp, width: 1600, height: 900, title: "4 · CEP infographic: timeline, mobility and plans A, B, C" }
  - { src: /assets/cep/slide-5.webp, width: 1600, height: 900, title: "5 · Bibliography" }
---

<section class="cep-block" markdown="1">

## 1. My CEP poster

From technician to engineer: where I come from, one mobility step abroad, and three five-year options. In my third year at ENSEEIHT (2027–2028), I will follow the **ACISE track** (*Architecture de Commande et Informatique des Systèmes Embarqués*: control architecture and embedded computing systems). Plan A is to grow within the VINCI Energies network and become a business manager.

</section>

<figure class="photo cep-poster">
  <a href="{% include image-url.html img=page.poster %}" data-lightbox="poster" data-caption="{{ page.poster.title }}">
    {% include image.html img=page.poster max=2000 sizes="(min-width: 1120px) 1072px, 100vw" %}
  </a>
</figure>
<p class="cep-actions"><a class="btn" href="{{ '/assets/cep/CEP_DUMAS_Maxime_poster.pdf' | relative_url }}" target="_blank" rel="noopener">Download the poster (PDF)</a></p>

<section class="cep-block" markdown="1">

## 2. Presentation for the 1 December jury

Five slides in English: one company one-pager, two slides of economic figures, my CEP infographic and the bibliography.

</section>

{% include gallery.html images=page.slides class="cep-slides" group="slides" sizes="(min-width: 960px) 50vw, 100vw" %}
<p class="cep-actions"><a class="btn btn-primary" href="{{ '/assets/cep/CEP_DUMAS_Maxime_slides.pdf' | relative_url }}" target="_blank" rel="noopener">Download the 5 slides (PDF)</a></p>

<section class="cep-block" markdown="1">

## 3. Mobility application — French and English

Priority target: a five-week secondment to **Axians Schweiz AG** (Le Mont-sur-Lausanne) in 2027. CV and cover letter tailored to this destination, in both languages. More details on my [Mobility page]({{ '/mobility/' | relative_url }}).

</section>

<div class="cv-grid cv-grid-4">
  {%- for c in site.data.mobility_docs %}
  <a class="cv-card" href="{{ c.url | relative_url }}" target="_blank" rel="noopener">
    <div class="cv-preview">
      {% include image.html img=c.preview max=700 sizes="(min-width: 960px) 240px, 45vw" %}
    </div>
    <div class="cv-info">
      <span class="cv-label">{{ c.label }}</span>
      <span class="muted">{{ c.lang }}</span>
    </div>
  </a>
  {%- endfor %}
</div>

<section class="cep-block" markdown="1">

## 4. CV and LinkedIn

</section>

<div class="cv-grid">
  {%- for c in site.cv %}
  <a class="cv-card" href="{{ c.url | relative_url }}" target="_blank" rel="noopener">
    <div class="cv-preview">
      {% include image.html img=c.preview max=700 sizes="(min-width: 800px) 260px, 45vw" %}
    </div>
    <div class="cv-info">
      <span class="cv-label">{% if c.lang == "English" %}CV — English{% else %}CV — Français{% endif %}</span>
      <span class="muted">General CV · PDF</span>
    </div>
  </a>
  {%- endfor %}
</div>
<p class="cep-actions"><a class="btn" href="{{ site.contact.linkedin }}" target="_blank" rel="noopener">My LinkedIn profile</a> <a class="btn" href="{{ '/press-review/' | relative_url }}">My Press Review</a></p>
