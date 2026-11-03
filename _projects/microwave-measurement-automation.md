---
title: "SAE SDK – Microwave Measurement Automation"
order: 4
year: "BUT3 - Semestre 5"
location: "BUT GEII - IUT Paul Sabatier"
type: "SAE"
summary: "Develop an object-oriented Python program to automate microwave measurements, mainly using a Vector Network Analyzer (VNA) and an oscilloscope."
cover:
  id: "3d2323_45de6a3c58ee4afe8a1a92a445ed68d8~mv2.png"
  width: 686
  height: 642
  fx: 0.53125
  fy: 0.6412639405204461
gallery:
  - id: "3d2323_f55ca972cb7245f3a28d0abb67d9faf6~mv2.png"
    width: 1313
    height: 796
    title: "Interface permettant de configurer la mesure à effectuer"
  - id: "3d2323_169ead24b90f4d23aa1edc09e11ba93f~mv2.png"
    width: 666
    height: 588
    title: "Exemple d'un rapport suite à l'utilisation du programme"
---

### Project Objective

Develop an object-oriented Python program to automate microwave measurements, mainly using a Vector Network Analyzer (VNA) and an oscilloscope.
The program was designed to allow a technician to easily run measurements, compare the results with specifications, and automatically export a report in Word or PDF.

### Achievements

- Designed an object-oriented architecture with a class diagram:
  - Instrument (VNA, Oscilloscope),
  - Measure (9 types of S-parameter measurements: S11, S21, bandwidth, rejection, etc.),
  - Result (visualization and plots),
  - Report (Word/PDF export).
- Implemented a command-line interface (interactive selector).
- Achieved full automation: instrument connection, calibration, measurements, graph generation, and result export.
- Conducted tests in simulation mode using the S2VNA DEMO software.

### Skills Developed

- Object-oriented programming in Python.
- Use of libraries: pyvisa, numpy, matplotlib, python-docx, docx2pdf.
- Instrument control and measurement (VNA, oscilloscope).
- Automated report generation and validation against specifications.
