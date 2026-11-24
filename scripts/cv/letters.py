"""Generate Maxime's mobility cover letters (EN, FR) with the same design as the CVs, then render PDFs."""
import pathlib, subprocess

HERE = pathlib.Path(__file__).parent
PORTFOLIO = "https://maximedumas46.github.io/e-portfolio/"
LINKEDIN = "https://www.linkedin.com/in/maxime-dumas-22b062258/"

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Inter", sans-serif; font-size: 10pt; line-height: 1.5; color: #1f2430; width: 210mm; height: 297mm; display: flex; }
a { color: inherit; text-decoration: none; }
.stripe { width: 8mm; background: #1c2333; position: relative; }
.stripe::after { content: ""; position: absolute; left: 0; right: 0; top: 18mm; height: 22mm; background: #f06aa9; }
.page { flex: 1; padding: 16mm 20mm 14mm 18mm; display: flex; flex-direction: column; }
.head { display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 5mm; border-bottom: 2px solid #a20067; }
h1 { font-size: 20pt; font-weight: 800; letter-spacing: .02em; color: #1c2333; line-height: 1.1; }
.title { color: #a20067; font-weight: 600; font-size: 9.5pt; margin: 1.2mm 0 2.5mm; }
.contact { font-size: 8.6pt; color: #5b6273; line-height: 1.55; }
.contact a { color: #1c2333; border-bottom: 1px solid #f06aa9; }
.to { text-align: right; font-size: 9.2pt; line-height: 1.55; margin-top: 1mm; }
.to b { color: #1c2333; }
.date { margin: 9mm 0 5mm; color: #5b6273; }
.subject { font-weight: 700; color: #1c2333; margin-bottom: 6mm; }
.subject span { color: #a20067; }
p { margin-bottom: 3.6mm; text-align: justify; }
.sign { margin-top: 5mm; font-weight: 700; color: #1c2333; }
"""

RECIPIENT = "<b>Ms Lara Ciurlia</b><br>Axians Schweiz AG<br>En Budron H10<br>CH-1052 Le Mont-sur-Lausanne<br>{country}"

LETTERS = {
 "DUMAS_Letter_Switzerland": dict(lang="en", title="Apprentice engineer · Axians / ENSEEIHT", country="Switzerland",
  recipient_name="Ms Lara Ciurlia", date="Toulouse, 24 November 2026",
  subject_label="Subject:", subject="5-week secondment within your mobile communication sites teams, 2027",
  body=[
   "Dear Ms Ciurlia,",
   "Axians Switzerland builds turnkey mobile communication sites for every Swiss network operator, from engineering to commissioning. In France I work on the power side of the same kind of sites: as an apprentice engineer at Axians Maintenance Infras Midi-Pyrénées, I bring Orange fixed-network sites back into electrical compliance across south-west France, and I work on the 48 V DC power systems that feed telecom sites for Orange, Bouygues Telecom, SFR and TOTEM. I would like to spend five weeks of 2027 in your Le Mont-sur-Lausanne branch.",
   "I can bring two things. First, practical experience of site power: on an Orange fibre site, I took part in an energy SWAP from survey to costing, then helped commission the new rectifiers and batteries and validated them by measurement (voltage, current, battery autonomy). Second, a solid electrical engineering background: at ENSEEIHT I study power electronics, electrical machines and control engineering, and during my bachelor's degree I automated microwave measurements with a Python program driving a vector network analyser. I am a native French speaker and work comfortably in English (TOEIC 895).",
   "Why now? My engineering degree at ENSEEIHT requires a period abroad, and my career plan is to become a business manager in the VINCI Energies network. Seeing how a sister company organises site construction and multi-operator 4G/5G rollouts is the best preparation for that role. I am discussing a secondment within the group with Axians France: my contract would stay active and my employer would keep paying my salary, so the stay would cost your team nothing beyond supervision.",
   "I would be glad to discuss dates and a suitable team with you. Thank you for your time and consideration.",
   "Yours sincerely,"]),
 "DUMAS_Lettre_Suisse": dict(lang="fr", title="Alternant ingénieur · Axians / ENSEEIHT", country="Suisse",
  recipient_name="Mme Lara Ciurlia", date="Toulouse, le 24 novembre 2026",
  subject_label="Objet :", subject="mise à disposition de cinq semaines au sein de vos équipes sites de communication mobile, 2027",
  body=[
   "Madame,",
   "Axians Suisse réalise des sites de communication mobile clés en main pour tous les opérateurs suisses, de l'ingénierie à la mise en service. En France, je travaille sur la partie énergie de ce même type de sites : alternant ingénieur chez Axians Maintenance Infras Midi-Pyrénées, je m'occupe de la remise en ordre électrique des sites fixes Orange dans le Sud-Ouest et j'interviens sur les systèmes d'énergie 48 V DC qui alimentent les sites télécoms d'Orange, Bouygues Telecom, SFR et TOTEM. Je souhaiterais passer cinq semaines en 2027 dans votre agence du Mont-sur-Lausanne.",
   "Je peux vous apporter deux choses. D'abord, une expérience concrète de l'énergie des sites : sur un site fibre Orange, j'ai participé à un SWAP énergie, du relevé au chiffrage, puis à la mise en service des nouveaux redresseurs et batteries, validée par des mesures (tension, courant, autonomie des batteries). Ensuite, une solide formation en génie électrique : à l'ENSEEIHT, j'étudie l'électronique de puissance, les machines électriques et l'automatique, et pendant mon BUT j'ai automatisé des mesures hyperfréquences avec un programme Python pilotant un analyseur de réseau vectoriel. Je travaille aussi à l'aise en anglais (TOEIC 895).",
   "Pourquoi maintenant ? Mon diplôme d'ingénieur de l'ENSEEIHT comprend une période à l'étranger, et mon projet professionnel est de devenir responsable d'affaires dans le réseau VINCI Energies. Découvrir comment une société sœur organise la construction de sites et les déploiements 4G/5G multi-opérateurs est la meilleure préparation à ce rôle. J'étudie avec Axians France une mise à disposition au sein du groupe : mon contrat resterait actif et mon employeur continuerait à me rémunérer, ce séjour ne coûterait donc rien à votre équipe en dehors de l'encadrement.",
   "Je serais heureux d'échanger avec vous sur les dates et l'équipe qui pourrait m'accueillir. Je vous remercie de l'attention que vous porterez à ma candidature et vous prie d'agréer, Madame, l'expression de mes salutations distinguées."]),
}

def letter(d):
    body = d["body"]
    paras = "".join(f"<p>{x}</p>" for x in body)
    to = RECIPIENT.replace("Ms Lara Ciurlia", d["recipient_name"]).format(country=d["country"])
    return f'''<!DOCTYPE html><html lang="{d["lang"]}"><head><meta charset="utf-8"><title>Maxime DUMAS – {"Cover letter" if d["lang"]=="en" else "Lettre de motivation"}</title><style>{CSS}</style></head>
<body><div class="stripe"></div><div class="page">
<div class="head"><div>
  <h1>MAXIME DUMAS</h1>
  <div class="title">{d["title"]}</div>
  <div class="contact">Toulouse, France · +33 6 28 18 14 95<br>
  <a href="mailto:maximedumas46@live.fr">maximedumas46@live.fr</a><br>
  <a href="{PORTFOLIO}">maximedumas46.github.io/e-portfolio</a> · <a href="{LINKEDIN}">LinkedIn</a></div>
</div><div class="to">{to}</div></div>
<div class="date">{d["date"]}</div>
<div class="subject"><span>{d["subject_label"]}</span> {d["subject"]}</div>
{paras}
<div class="sign">Maxime Dumas</div>
</div></body></html>'''

out = HERE / "out"; out.mkdir(exist_ok=True)
for name, d in LETTERS.items():
    (out / f"{name}.html").write_text(letter(d))
subprocess.run(["node", "-e", """
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
for (const n of process.argv.slice(1)) { await p.goto('file://'+n+'.html'); await p.pdf({path:n+'.pdf',format:'A4',printBackground:true});
const o=await p.evaluate(()=>{const s=document.querySelector('.sign').getBoundingClientRect(); return Math.round(s.bottom)+' / '+document.body.clientHeight}); console.log(n.split('/').pop(), 'sign bottom', o); }
await b.close()})()""", *[str(out / n) for n in LETTERS]], check=True)
