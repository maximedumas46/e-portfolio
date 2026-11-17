---
title: "Electrical Machines – Models and Prototype"
order: 3
year: "ENSEEIHT – 2A (2026)"
location: "INP ENSEEIHT, Toulouse"
type: "Lab work and micro-project (in progress)"
summary: "Induction machine efficiency, variable-speed drive control laws and stand-alone induction generator, plus the design, winding and testing of an axial-flux synchronous motor (MicroMAG)."
cover:
  src: /assets/img/projects/machines/micromag-bench.webp
  width: 593
  height: 439
  alt: "MicroMAG axial-flux motor test bench"
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
  - src: /assets/img/projects/machines/micromag-winding.webp
    width: 844
    height: 983
    title: "MicroMAG: hand-wound three-phase stator"
  - src: /assets/img/projects/machines/micromag-emf.webp
    width: 658
    height: 426
    title: "MicroMAG: back-EMF of two phases"
  - src: /assets/img/projects/machines/micromag-plate.webp
    width: 1380
    height: 659
    title: "MicroMAG: nameplate of our prototype"
---

### Project Objective

Link the models of electrical machines seen in class to their real behaviour on the test bench. Carried out with Patrice Masson (and Roch Berquieres for TP3). The lab series is still in progress: this page will grow with the next sessions.

### TP3 – Induction Machine: Efficiency, Control Laws and Stand-alone Generator

**Induction motor coupled to an active load**

- Read the nameplate and chose the star connection for a 400 V supply; wired the induction motor and a permanent magnet synchronous machine (PMSM) used as load, each on its own variable-speed drive.
- Measured the nominal point (≈ 10 N·m, 1 430 rpm, efficiency ≈ 75–80 %) and compared three measurement chains: Fluke 435 analyser, drive software and torque sensor.
- Compared the drive's two open-loop control modes (U/f "fixed" and "U·I" with stator-voltage compensation) across the speed range: the U·I mode avoids the power drop and the overload trip at low speed.

**Induction machine as a stand-alone generator**

- Calculated the reactive power needed to magnetise the machine and sized the capacitor bank (star vs delta connection).
- Self-excitation tests: the generator builds up its voltage from about 30–35 % of the capacitor bank; then load tests showing the voltage collapse and de-excitation when active power increases.
- Voltage versus speed hysteresis, and conclusion: on an isolated site, an induction generator needs adjustable capacitors with voltage regulation, and a synchronous machine is often a better choice.

### Micro-project – MicroMAG Axial-Flux Synchronous Motor

- **Understand:** magnetic circuit of an axial-flux permanent magnet machine, from Laplace forces to torque.
- **Design:** calculated the air-gap flux density (≈ 0.37 T) and the number of turns needed for a target torque of 85 mN·m per phase at 2.5 A.
- **Build:** wound the three phases by hand (30 turns per phase, two slots per pole and per phase) and checked continuity, winding direction and phase shift.
- **Supply:** self-controlled supply by six reed switches driven by the rotor position (120° commutation), with adjustment of the commutation angle.
- **Characterise:** back-EMF constant (≈ 0.027 V·s/rad, 8 % below the model), static torque of 182.6 mN·m, no-load speed of 360 rpm, power balance and a nameplate for the prototype, plus ideas to improve its efficiency.

### Skills Developed

- Electrical machines: induction and synchronous machines, equivalent circuits, magnetic circuits.
- Variable-speed drives and their control laws.
- Power and efficiency measurements (power analyser, torque sensor, spring balance).
- Hands-on prototyping: winding, wiring, commissioning and comparing a model with test results.
