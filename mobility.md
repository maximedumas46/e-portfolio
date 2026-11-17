---
layout: page
title: Mobility
permalink: /mobility/
logo:
  id: "3d2323_cde468016ab74e43928834f9a991615b~mv2.webp"
  width: 1920
  height: 1080
  alt: "Axians"
mobility_docs:
  - label: CV — Switzerland
    lang: English · tailored · PDF
    url: /assets/mobility/DUMAS_CV_Switzerland.pdf
    preview: { src: /assets/mobility/preview-cv.webp, width: 494, height: 700, alt: "Preview of the tailored CV" }
  - label: Cover letter — Switzerland
    lang: English · PDF
    url: /assets/mobility/DUMAS_Letter_Switzerland.pdf
    preview: { src: /assets/mobility/preview-letter.webp, width: 494, height: 700, alt: "Preview of the cover letter" }
---

<section class="prose" markdown="1">

### My Current Progress

I spent four weeks in Barcelona. This experience was particularly enriching thanks to the international team of volunteers I worked alongside, each bringing their own culture and way of doing things, which taught me a lot about adapting to different working styles. Since I didn't speak Spanish, I communicated in English throughout my stay, which pushed me out of my comfort zone and significantly improved my confidence speaking English day to day. Beyond the practical tasks, this kind of volunteering builds autonomy, teamwork, and the ability to find your bearings in a new environment with the language barrier being, by far, the biggest challenge to overcome.

</section>

<section class="next-mobility">
  <div class="next-mobility-logo">
    {% include image.html img=page.logo max=640 sizes="200px" %}
  </div>
  <div class="prose" markdown="1">

For the next mobility, I have already discussed opportunities with my company, Axians, and there may be openings within the VINCI group. We are looking at a **secondment** (*mise à disposition*, Art. L6222-42 of the French Labour Code) to another VINCI Energies subsidiary abroad: my apprenticeship contract would remain active, Axians would keep paying my salary and maintain my social protection, and a secondment agreement would be signed with the host company. My priority target is now **Axians Schweiz AG** in Switzerland (details below); the final choice still depends on my employer's agreement and on ENSEEIHT's selection.

  </div>
</section>

<section class="prose" markdown="1">

## International mobility 2027-2028

- **Route:** placement abroad, as a secondment (*mise à disposition*) within the VINCI Energies group
- **Duration:** 5 weeks in 2027, completing the 4 weeks already done in Barcelona
- **Priority destination:** **Axians Schweiz AG**, Le Mont-sur-Lausanne (French-speaking Switzerland)
- **Back-up:** Axians Schweiz AG, Vernier branch (Geneva)
- **Status:** target defined; employer agreement and ENSEEIHT selection in progress

**Why this company?** Axians Switzerland designs, builds and operates mobile communication sites for every Swiss network operator. My business unit in Toulouse maintains the 48 V DC power systems of the same kind of sites for Orange, Bouygues Telecom, SFR and TOTEM. Spending five weeks on the construction side would show me the full life of a telecom site, from engineering to commissioning, which is exactly what a business manager in the VINCI Energies network needs to understand.

**Five keywords:** mobile communication sites · 48 V DC power · multi-operator 4G/5G · commissioning & measurements · turnkey site construction

</section>

<div class="mobility-docs" style="margin-top:24px">
  <div class="cv-grid">
    {%- for c in page.mobility_docs %}
    <a class="cv-card" href="{{ c.url | relative_url }}" target="_blank" rel="noopener">
      <div class="cv-preview">
        {% include image.html img=c.preview max=700 sizes="(min-width: 800px) 260px, 45vw" %}
      </div>
      <div class="cv-info">
        <span class="cv-label">{{ c.label }}</span>
        <span class="muted">{{ c.lang }}</span>
      </div>
    </a>
    {%- endfor %}
  </div>
</div>

