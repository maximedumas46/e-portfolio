---
layout: page
title: Sports
permalink: /sports/
intro: In this section, I share some of my road bike rides that stood out for their intensity and the challenges they represented.
rides:
  - title: Crossing the Pyrenees
    photos:
      - id: "3d2323_0198eb750f6d45be9e11d6effc141871~mv2.png"
        width: 2286
        height: 1067
        alt: "Route map — Crossing the Pyrenees"
      - id: "3d2323_010339dc46b64552926b37374f0883c2~mv2.jpg"
        width: 1028
        height: 1374
        alt: "At the summit — Crossing the Pyrenees"
  - title: Col d'Aubisque
    photos:
      - id: "3d2323_ad7dbac202f74bafa80dff81ec95d13a~mv2.png"
        width: 838
        height: 688
        alt: "Route map — Col d'Aubisque"
      - id: "3d2323_8ba06db2f9f84814aca6ad80cc749482~mv2.jpg"
        width: 1152
        height: 2048
        alt: "Kilometre marker — Col d'Aubisque"
---

<div class="rides">
{%- for ride in page.rides %}
<article class="ride">
<h2>{{ ride.title }}</h2>
{% include gallery.html images=ride.photos class="ride-photos" group=ride.title sizes="(min-width: 960px) 50vw, 100vw" %}
</article>
{%- endfor %}
</div>
