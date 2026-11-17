---
title: "Machine Models – Induction Machine"
order: 3
year: "ENSEEIHT – 2A (2026)"
location: "INP ENSEEIHT, Toulouse"
type: "Lab work (in progress)"
summary: "Efficiency and variable-speed drive control laws of an induction motor, then the same machine used as a stand-alone generator with a capacitor bank."
cover:
  src: /assets/img/projects/machines/bench-drives.webp
  width: 988
  height: 741
  alt: "Induction machine test bench with variable-speed drives"
gallery:
  - src: /assets/img/projects/machines/bench-drives.webp
    width: 988
    height: 741
    title: "Test bench: two variable-speed drives and a Fluke 435 analyser"
  - src: /assets/img/projects/machines/pmsm-torque.webp
    width: 915
    height: 686
    title: "Permanent magnet synchronous machine used as active load"
  - src: /assets/img/projects/machines/fluke-motor.webp
    width: 1204
    height: 917
    title: "Motor analysis on the Fluke 435"
  - src: /assets/img/projects/machines/power-speed.webp
    width: 925
    height: 707
    title: "Power versus speed for two drive control modes"
  - src: /assets/img/projects/machines/capacitor-bank.webp
    width: 687
    height: 515
    title: "Capacitor bank used to self-excite the induction generator"
  - src: /assets/img/projects/machines/u-vs-p.webp
    width: 841
    height: 628
    title: "Generator voltage versus active power"
  - src: /assets/img/projects/machines/hysteresis.webp
    width: 889
    height: 540
    title: "Voltage versus speed: self-excitation hysteresis"



---

### Project Objective

Link the models of electrical machines seen in class to their real behaviour on the test bench. Carried out with Patrice Masson and Roch Berquieres. The lab series is still in progress: this page will grow with the next sessions.

### TP3 – Induction Machine: Efficiency, Control Laws and Stand-alone Generator

**Induction motor coupled to an active load**

- Read the nameplate and chose the star connection for a 400 V supply; wired the induction motor and a permanent magnet synchronous machine (PMSM) used as load, each on its own variable-speed drive.
- Measured the nominal point (≈ 10 N·m, 1 430 rpm, efficiency ≈ 75–80 %) and compared three measurement chains: Fluke 435 analyser, drive software and torque sensor.
- Compared the drive's two open-loop control modes (U/f "fixed" and "U·I" with stator-voltage compensation) across the speed range: the U·I mode avoids the power drop and the overload trip at low speed.

**Induction machine as a stand-alone generator**

- Calculated the reactive power needed to magnetise the machine and sized the capacitor bank (star vs delta connection).
- Self-excitation tests: the generator builds up its voltage from about 30–35 % of the capacitor bank; then load tests showing the voltage collapse and de-excitation when active power increases.
- Voltage versus speed hysteresis, and conclusion: on an isolated site, an induction generator needs adjustable capacitors with voltage regulation, and a synchronous machine is often a better choice.


### Skills Developed

- Induction machine: equivalent circuit, slip, efficiency, reactive power and self-excitation.
- Variable-speed drives and their control laws.
- Power and efficiency measurements (power analyser, torque sensor).
- Wiring and commissioning a power test bench, and comparing models with measurements.
