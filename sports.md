---
layout: page
title: Sports
permalink: /sports/
intro: In this section, I share some of my road bike rides that stood out for their intensity and the challenges they represented.
rides:
  - title: Crossing the Pyrenees
    map:
      id: "3d2323_0198eb750f6d45be9e11d6effc141871~mv2.png"
      width: 2286
      height: 1067
      alt: "Route map — Crossing the Pyrenees"
    photos:
      - id: "3d2323_010339dc46b64552926b37374f0883c2~mv2.jpg"
        width: 1028
        height: 1374
        alt: "At the top of a Pyrenean col"
      - id: "3d2323_8ba06db2f9f84814aca6ad80cc749482~mv2.jpg"
        width: 1152
        height: 2048
        alt: "Col d'Aubisque sign"
  - title: Brevet de Randonneur Mondial — 300 km
    map:
      id: "3d2323_ad7dbac202f74bafa80dff81ec95d13a~mv2.png"
      width: 838
      height: 688
      alt: "Route map — Brevet de Randonneur Mondial 300 km"
---

<div class="rides">
{%- for ride in page.rides %}
<article class="ride">
<h2>{{ ride.title }}</h2>
{%- if ride.map %}
<figure class="ride-map">
<a href="{% include image-url.html img=ride.map %}" data-lightbox="{{ ride.title | escape }}" data-caption="{{ ride.map.alt | escape }}">
{% include image.html img=ride.map max=1600 sizes="(min-width: 1120px) 1072px, 100vw" %}
</a>
</figure>
{%- endif %}
{%- if ride.photos and ride.photos.size > 0 %}
{% include gallery.html images=ride.photos class="ride-photos" group=ride.title sizes="(min-width: 960px) 520px, 50vw" %}
{%- endif %}
</article>
{%- endfor %}
</div>
