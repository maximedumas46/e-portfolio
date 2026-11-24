// Simple, professional Word cover letters (EN + FR) for the Axians Schweiz mobility application.
const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, AlignmentType, ExternalHyperlink } = require('docx');

const FONT = 'Calibri';
const SIZE = 22; // 11 pt

const sender = [
  'Maxime DUMAS',
  'Toulouse, France',
  '+33 6 28 18 14 95',
  'maximedumas46@live.fr',
  'maximedumas46.github.io/e-portfolio',
];

const L = {
  en: {
    file: 'DUMAS_Letter_Switzerland',
    recipient: ['Ms Lara Ciurlia', 'Axians Schweiz AG', 'En Budron H10', 'CH-1052 Le Mont-sur-Lausanne', 'Switzerland'],
    date: 'Toulouse, 24 November 2026',
    subjectLabel: 'Subject: ',
    subject: '5-week secondment within your mobile communication sites teams, 2027',
    body: [
      'Dear Ms Ciurlia,',
      'Axians Switzerland builds turnkey mobile communication sites for every Swiss network operator, from engineering to commissioning. In France I work on the power side of the same kind of sites: as an apprentice engineer at Axians Maintenance Infras Midi-Pyrénées, I bring Orange fixed-network sites back into electrical compliance across south-west France, and I work on the 48 V DC power systems that feed telecom sites for Orange, Bouygues Telecom, SFR and TOTEM. I would like to spend five weeks of 2027 in your Le Mont-sur-Lausanne branch.',
      'I can bring two things. First, practical experience of site power: on an Orange fibre site, I took part in an energy SWAP from survey to costing, then helped commission the new rectifiers and batteries and validated them by measurement (voltage, current, battery autonomy). Second, a solid electrical engineering background: at ENSEEIHT I study power electronics, electrical machines and control engineering, and during my bachelor’s degree I automated microwave measurements with a Python program driving a vector network analyser. I am a native French speaker and work comfortably in English (TOEIC 895).',
      'Why now? My engineering degree at ENSEEIHT requires a period abroad, and my career plan is to become a business manager in the VINCI Energies network. Seeing how a sister company organises site construction and multi-operator 4G/5G rollouts is the best preparation for that role. I am discussing a secondment within the group with Axians France: my contract would stay active and my employer would keep paying my salary, so the stay would cost your team nothing beyond supervision.',
      'I would be glad to discuss dates and a suitable team with you. Thank you for your time and consideration.',
      'Yours sincerely,',
    ],
  },
  fr: {
    file: 'DUMAS_Lettre_Suisse',
    recipient: ['Madame Lara Ciurlia', 'Axians Schweiz AG', 'En Budron H10', 'CH-1052 Le Mont-sur-Lausanne', 'Suisse'],
    date: 'Toulouse, le 24 novembre 2026',
    subjectLabel: 'Objet : ',
    subject: 'mise à disposition de cinq semaines au sein de vos équipes sites de communication mobile, 2027',
    body: [
      'Madame,',
      'Axians Suisse réalise des sites de communication mobile clés en main pour tous les opérateurs suisses, de l’ingénierie à la mise en service. En France, je travaille sur la partie énergie de ce même type de sites : alternant ingénieur chez Axians Maintenance Infras Midi-Pyrénées, je m’occupe de la remise en ordre électrique des sites fixes Orange dans le Sud-Ouest et j’interviens sur les systèmes d’énergie 48 V DC qui alimentent les sites télécoms d’Orange, Bouygues Telecom, SFR et TOTEM. Je souhaiterais passer cinq semaines en 2027 dans votre agence du Mont-sur-Lausanne.',
      'Je peux vous apporter deux choses. D’abord, une expérience concrète de l’énergie des sites : sur un site fibre Orange, j’ai participé à un SWAP énergie, du relevé au chiffrage, puis à la mise en service des nouveaux redresseurs et batteries, validée par des mesures (tension, courant, autonomie des batteries). Ensuite, une solide formation en génie électrique : à l’ENSEEIHT, j’étudie l’électronique de puissance, les machines électriques et l’automatique, et pendant mon BUT j’ai automatisé des mesures hyperfréquences avec un programme Python pilotant un analyseur de réseau vectoriel. Je travaille aussi à l’aise en anglais (TOEIC 895).',
      'Pourquoi maintenant ? Mon diplôme d’ingénieur de l’ENSEEIHT comprend une période à l’étranger, et mon projet professionnel est de devenir responsable d’affaires dans le réseau VINCI Energies. Découvrir comment une société sœur organise la construction de sites et les déploiements 4G/5G multi-opérateurs est la meilleure préparation à ce rôle. J’étudie avec Axians France une mise à disposition au sein du groupe : mon contrat resterait actif et mon employeur continuerait à me rémunérer, ce séjour ne coûterait donc rien à votre équipe en dehors de l’encadrement.',
      'Je serais heureux d’échanger avec vous sur les dates et l’équipe qui pourrait m’accueillir. Je vous remercie de l’attention que vous porterez à ma candidature et vous prie d’agréer, Madame, l’expression de mes salutations distinguées.',
    ],
  },
};

const line = (text, opts = {}) => new Paragraph({
  alignment: AlignmentType.LEFT,
  indent: opts.indent ? { left: opts.indent } : undefined,
  spacing: { before: 0, after: opts.after || 0, line: 264 },
  children: [new TextRun({ text, bold: !!opts.bold, font: FONT, size: SIZE })],
});

function build(d) {
  const children = [];
  sender.forEach((t, i) => children.push(line(t, { bold: i === 0 })));
  children.push(line('', { after: 240 }));
  d.recipient.forEach((t, i) => children.push(line(t, { indent: 5103, bold: i === 0 })));
  children.push(line('', { after: 240 }));
  children.push(line(d.date, { indent: 5103, after: 360 }));
  children.push(new Paragraph({
    spacing: { before: 0, after: 360, line: 264 },
    children: [
      new TextRun({ text: d.subjectLabel, bold: true, font: FONT, size: SIZE }),
      new TextRun({ text: d.subject, bold: true, font: FONT, size: SIZE }),
    ],
  }));
  d.body.forEach((t, i) => children.push(new Paragraph({
    alignment: i === 0 || i === d.body.length - 1 && t.length < 30 ? AlignmentType.LEFT : AlignmentType.JUSTIFIED,
    spacing: { before: 0, after: 200, line: 276 },
    children: [new TextRun({ text: t, font: FONT, size: SIZE })],
  })));
  children.push(line('', { after: 240 }));
  children.push(line('Maxime Dumas'));
  return new Document({
    creator: 'Maxime Dumas',
    title: d.file,
    styles: { default: { document: { run: { font: FONT, size: SIZE } } } },
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1417, bottom: 1417, left: 1417, right: 1417 } } },
      children,
    }],
  });
}

const out = path.join(__dirname, 'out');
(async () => {
  for (const k of ['en', 'fr']) {
    const buf = await Packer.toBuffer(build(L[k]));
    fs.writeFileSync(path.join(out, L[k].file + '.docx'), buf);
    console.log('wrote', L[k].file + '.docx');
  }
})();
