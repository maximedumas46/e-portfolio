"""Generate Maxime's CVs (EN, FR, Switzerland) with one shared design, then render PDFs."""
import base64, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent
PHOTO = base64.b64encode((HERE / "photo.jpg").read_bytes()).decode()
PORTFOLIO = "https://maximedumas46.github.io/e-portfolio/"
LINKEDIN = "https://www.linkedin.com/in/maxime-dumas-22b062258/"

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Inter", sans-serif; font-size: 8.5pt; line-height: 1.36; color: #1f2430; width: 210mm; height: 297mm; display: flex; }
a { color: inherit; text-decoration: none; }
.side { width: 62mm; background: #1c2333; color: #e8ebf2; padding: 10mm 6mm 8mm 8mm; }
.photo { width: 36mm; height: 36mm; border-radius: 50%; object-fit: cover; display: block; margin: 0 auto 6mm; border: 2px solid #f06aa9; }
.main { flex: 1; padding: 11mm 9mm 8mm 9mm; }
.side h2 { color: #f06aa9; font-size: 8.4pt; letter-spacing: .12em; font-weight: 700; padding-bottom: 2mm; border-bottom: 1px solid #3a4358; margin: 5.2mm 0 2.4mm; }
.side h2.first { margin-top: 0; }
.side p { margin-bottom: 1.5mm; font-size: 8pt; }
.side b { color: #fff; }
.side a { color: #fff; border-bottom: 1px solid #f06aa9; }
.lbl { display: block; color: #9aa3b8; font-size: 7pt; letter-spacing: .06em; text-transform: uppercase; }
h1 { font-size: 22pt; font-weight: 800; letter-spacing: .02em; color: #1c2333; }
.title { color: #a20067; font-weight: 600; font-size: 10pt; margin-top: 1mm; }
.target { color: #5b6273; font-size: 8.2pt; margin-top: 1.4mm; }
.main h2 { color: #a20067; font-size: 8.6pt; letter-spacing: .12em; font-weight: 700; padding-bottom: 1.4mm; border-bottom: 1px solid #e3e5ec; margin: 4.4mm 0 2.1mm; }
.hl { color: #a20067; font-weight: 600; }
.row { display: flex; justify-content: space-between; align-items: baseline; margin-top: 2.1mm; }
.main h2 + .row { margin-top: 0; }
.date { color: #5b6273; font-size: 8pt; white-space: nowrap; margin-left: 3mm; }
.n { font-weight: 400; }
.sub { font-style: italic; color: #5b6273; }
ul { padding-left: 4.2mm; margin-top: .7mm; }
li { margin-bottom: .6mm; }
"""

def entry(title, date, sub=None, bullets=()):
    h = f'<div class="row"><b>{title}</b><span class="date">{date}</span></div>'
    if sub: h += f'<div class="sub">{sub}</div>'
    if bullets: h += "<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>"
    return h

T = {
 "en": dict(contact="CONTACT", portfolio="Portfolio", tech="TECHNICAL SKILLS", lang="LANGUAGES", pers="PERSONAL SKILLS",
            inter="INTERESTS", profile="PROFILE", exp="PROFESSIONAL EXPERIENCE", edu="EDUCATION", vol="VOLUNTEERING",
            licence="Driving licence: category B"),
 "fr": dict(contact="CONTACT", portfolio="Portfolio", tech="COMPÉTENCES TECHNIQUES", lang="LANGUES", pers="QUALITÉS",
            inter="CENTRES D'INTÉRÊT", profile="PROFIL", exp="EXPÉRIENCES PROFESSIONNELLES", edu="FORMATION", vol="BÉNÉVOLAT",
            licence="Permis B"),
}

SIDE = {
 "en": dict(
  tech=['<b>Electrical installations:</b> bringing sites into compliance, protections (Schneider)',
        '<b>48 V DC power systems:</b> rectifiers (Eltek / Delta), batteries, DC distribution',
        '<b>Measurements:</b> voltage, current, battery autonomy; multimeter, oscilloscope',
        '<b>Programming:</b> Python, C++, STM32CubeIDE, Vivado (VHDL), Proteus',
        '<b>Office:</b> Microsoft 365, technical reporting, cost estimates'],
  lang=['<b>French:</b> native', '<b>English:</b> B2, TOEIC 895 / 990; working language during 4 weeks abroad', '<b>Chinese:</b> A2'],
  pers=['Reliable, quality-minded', 'Teamwork, active listening', 'Autonomous and organised'],
  inter=['Cycling: Cahors Cycling Club, 300 km badge', 'Badminton', 'Flight simulation (X-Plane, MSFS)']),
 "fr": dict(
  tech=['<b>Installations électriques :</b> remise en conformité de sites, protections (Schneider)',
        '<b>Énergie 48 V DC :</b> redresseurs (Eltek / Delta), batteries, distribution DC',
        '<b>Mesures :</b> tension, courant, autonomie batteries ; multimètre, oscilloscope',
        '<b>Programmation :</b> Python, C++, STM32CubeIDE, Vivado (VHDL), Proteus',
        '<b>Bureautique :</b> Microsoft 365, rapports techniques, chiffrage'],
  lang=['<b>Français :</b> langue maternelle', '<b>Anglais :</b> B2, TOEIC 895 / 990 ; langue de travail pendant 4 semaines à l\'étranger', '<b>Chinois :</b> A2'],
  pers=['Sérieux, souci du travail de qualité', 'Travail en équipe, écoute', 'Autonome et organisé'],
  inter=['Cyclisme : Cahors Cyclisme, Brevet randonneur mondial 300 km', 'Badminton', 'Simulation aéronautique (X-Plane, MSFS)']),
}

def axians(lang, swiss=False):
    if lang == "en":
        b = ['In charge of bringing <b>Orange fixed-network sites back into electrical compliance</b> across south-west France, from about an hour north of Brive down to the Pyrenees.',
             'Carried out an <b>energy SWAP on an Orange fibre site</b> with a technical manager: surveyed the existing rectifiers, batteries and DC board, defined the replacement equipment and estimated cost and intervention time.',
             'Prepared the <span class="hl">commissioning</span>: DC wiring checks and validation measurements (voltage, current, battery autonomy); updated the site documentation to the operator\'s standards.',
             'Support the business manager on <b>preventive and corrective maintenance contracts</b> for fixed and mobile operators: technical analysis, budgeting, coordination of interventions.']
        return entry('Axians Maintenance Infras Midi-Pyrénées <span class="n">(VINCI Energies)</span>', '2025 – present',
                     'Engineering apprentice · SAS Santerne Toulouse · Quint-Fonsegrives', b)
    b = ['Chargé de la <b>remise en ordre électrique des sites fixes Orange</b> dans le Sud-Ouest, d\'environ une heure au nord de Brive jusqu\'aux Pyrénées.',
         'Réalisation d\'un <b>SWAP énergie sur un site fibre Orange</b> avec un chargé d\'affaires : relevé des redresseurs, batteries et tableau DC existants, choix du matériel de remplacement, chiffrage et estimation du temps d\'intervention.',
         'Préparation de la <span class="hl">mise en service</span> : contrôle du câblage DC et mesures de validation (tension, courant, autonomie batteries) ; mise à jour du dossier de site aux standards de l\'opérateur.',
         'Appui au responsable d\'affaires sur les <b>contrats de maintenance préventive et corrective</b> des opérateurs fixes et mobiles : étude technique, chiffrage, organisation des interventions.']
    return entry('Axians Maintenance Infras Midi-Pyrénées <span class="n">(VINCI Energies)</span>', '2025 – présent',
                 'Alternant ingénieur · SAS Santerne Toulouse · Quint-Fonsegrives', b)

def continental(lang):
    if lang == "en":
        return entry('Continental AG <span class="n">– Toulouse</span>', '2023 – 2025', 'Apprentice diagnostic technician',
            ['Diagnosed defective electronic parts from production lines with measurement instruments; wrote defect reports.',
             'Carried out <b>preventive and corrective maintenance</b> on production test racks and changed test configurations.'])
    return entry('Continental AG <span class="n">– Toulouse</span>', '2023 – 2025', 'Alternant technicien diagnostiqueur',
        ['Diagnostic des pièces électroniques défectueuses issues des lignes de production à l\'aide d\'appareils de mesure ; rédaction de comptes rendus de défauts.',
         '<b>Maintenance préventive et corrective</b> des baies de test des chaînes de production et changements de configuration de test.'])

def education(lang):
    if lang == "en":
        return (entry('Engineering degree, Electrical Engineering – INP ENSEEIHT', '2025 – 2028',
                      'Electrical Engineering (GE) track, 3EA department · apprenticeship programme alternating school and company',
                      ['Power electronics (various converters), electrical machines, automation and control engineering, microcontroller programming, VHDL.'])
              + entry('BUT GEII – IUT, University of Toulouse', '2022 – 2025',
                      'Electrical Engineering &amp; Industrial Computing, embedded systems track · apprenticeship · High honours, ranked 3/38',
                      ['Embedded programming (STM32, C++, VHDL), electronics and instrumentation.',
                       'Project: Python program driving a vector network analyser and an oscilloscope to automate microwave measurements and reports.'])
              + entry('General Baccalaureate <span class="n">– Lycée Clément Marot, Cahors</span>', '2022',
                      'Mathematics, Physics-Chemistry, English · Honours'))
    return (entry('Diplôme d\'ingénieur, Génie Électrique – INP ENSEEIHT', '2025 – 2028',
                  'Filière Génie Électrique (GE), département 3EA · formation par apprentissage',
                  ['Électronique de puissance (différents convertisseurs), machines électriques, automatisme et automatique, programmation de microcontrôleurs, VHDL.'])
          + entry('BUT GEII – IUT de l\'Université de Toulouse', '2022 – 2025',
                  'Génie Électrique et Informatique Industrielle, parcours Électronique et Systèmes Embarqués · alternance · Mention Très bien, rang 3/38',
                  ['Programmation embarquée (STM32, C++, VHDL), électronique et instrumentation.',
                   'Projet : programme Python pilotant un analyseur de réseau vectoriel et un oscilloscope pour automatiser des mesures hyperfréquences et leurs rapports.'])
          + entry('Baccalauréat général <span class="n">– Lycée Clément Marot, Cahors</span>', '2022',
                  'Spécialités Mathématiques, Physique-Chimie, Anglais · Mention Bien'))

def volunteering(lang):
    if lang == "en":
        return (entry('Food Rescue &amp; Animal Care – Barcelona, Spain <span class="n">(ImpacTrip)</span>', '2026 · 4 weeks', None,
                      ['Collected unsold food from local shops to prepare baskets for families in need, and cared for animals at a cat shelter, in an international team working in English.'])
              + entry('Sports events – Cahors area', '2016 – 2024', None,
                      ['Volunteer at the Ekiden de Cahors, Trail des Collines du Diable and Raid Nature 46.']))
    return (entry('Food Rescue &amp; Animal Care – Barcelone, Espagne <span class="n">(ImpacTrip)</span>', '2026 · 4 semaines', None,
                  ['Collecte d\'invendus auprès des commerces pour préparer des colis destinés à des familles en difficulté, et soins aux animaux d\'un refuge pour chats, au sein d\'une équipe internationale, en anglais.'])
          + entry('Événements sportifs – Cahors et alentours', '2016 – 2024', None,
                  ['Bénévole à l\'Ekiden de Cahors, au Trail des Collines du Diable et au Raid Nature 46.']))

def page(lang, title, subtitle, profile, target=None):
    t, s = T[lang], SIDE[lang]
    side = f'''<aside class="side">
  <img class="photo" src="data:image/jpeg;base64,{PHOTO}" alt="Maxime Dumas">
  <h2 class="first">{t["contact"]}</h2>
  <p>Toulouse, France</p>
  <p>+33 6 28 18 14 95</p>
  <p><a href="mailto:maximedumas46@live.fr">maximedumas46@live.fr</a></p>
  <p><span class="lbl">{t["portfolio"]}</span><a href="{PORTFOLIO}">maximedumas46.github.io/e-portfolio</a></p>
  <p><span class="lbl">LinkedIn</span><a href="{LINKEDIN}">linkedin.com/in/maxime-dumas-22b062258</a></p>
  <p>{t["licence"]}</p>
  <h2>{t["tech"]}</h2>{"".join(f"<p>{x}</p>" for x in s["tech"])}
  <h2>{t["lang"]}</h2>{"".join(f"<p>{x}</p>" for x in s["lang"])}
  <h2>{t["pers"]}</h2>{"".join(f"<p>{x}</p>" for x in s["pers"])}
  <h2>{t["inter"]}</h2>{"".join(f"<p>{x}</p>" for x in s["inter"])}
</aside>'''
    main = f'''<main class="main">
  <h1>MAXIME DUMAS</h1>
  <div class="title">{subtitle}</div>
  {f'<div class="target">{target}</div>' if target else ''}
  <h2>{t["profile"]}</h2><p>{profile}</p>
  <h2>{t["exp"]}</h2>{axians(lang)}{continental(lang)}
  <h2>{t["edu"]}</h2>{education(lang)}
  <h2>{t["vol"]}</h2>{volunteering(lang)}
</main>'''
    return f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head><body>{side}{main}</body></html>'

CVS = {
 "CV_DUMAS_MAXIME_ENGLISH": page("en", "Maxime DUMAS – CV",
    "Engineering Apprentice · Electrical Engineering &amp; Telecom Site Power",
    'Electrical engineering apprentice at ENSEEIHT, working at Axians in Toulouse on the <span class="hl">electrical installations</span> and <span class="hl">48 V DC power systems</span> that keep fixed and mobile telecom sites running for Orange, Bouygues Telecom, SFR and TOTEM. Rigorous and autonomous on site, I am building a profile that combines field work, technical analysis and project coordination.'),
 "CV_DUMAS_MAXIME_FRANCAIS": page("fr", "Maxime DUMAS – CV",
    "Alternant ingénieur · Génie électrique &amp; énergie des sites télécoms",
    'Alternant ingénieur en génie électrique à l\'ENSEEIHT, je travaille chez Axians à Toulouse sur les <span class="hl">installations électriques</span> et les <span class="hl">systèmes d\'énergie 48 V DC</span> des sites télécoms fixes et mobiles d\'Orange, Bouygues Telecom, SFR et TOTEM. Rigoureux et autonome sur le terrain, je construis un profil qui allie intervention sur site, étude technique et coordination de projets.'),
 "DUMAS_CV_Switzerland": page("en", "Maxime DUMAS – CV",
    "Apprentice Engineer · Telecom Site Power &amp; Infrastructure",
    'Electrical engineering apprentice at ENSEEIHT, working at Axians in Toulouse on the <span class="hl">electrical installations</span> and <span class="hl">48 V DC power systems</span> that keep fixed and mobile telecom sites running for Orange, Bouygues Telecom, SFR and TOTEM. I want to see how Axians Switzerland builds <span class="hl">turnkey mobile communication sites</span> for all Swiss operators, and bring back methods to my business unit in France.',
    target='Target: 5-week secondment to <b>Axians Schweiz AG</b>, mobile communication sites, Le Mont-sur-Lausanne · 2027'),
}

out = HERE / "out"; out.mkdir(exist_ok=True)
for name, html in CVS.items():
    (out / f"{name}.html").write_text(html)
subprocess.run(["node", "-e", """
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
for (const n of process.argv.slice(1)) { await p.goto('file://'+n+'.html'); await p.pdf({path:n+'.pdf',format:'A4',printBackground:true});
const o=await p.evaluate(()=>[document.querySelector('.main').scrollHeight,document.querySelector('.side').scrollHeight,document.body.clientHeight]); console.log(n.split('/').pop(),o); }
await b.close()})()""", *[str(out / n) for n in CVS]], check=True)
