---
title: "MicroMAG – Axial-Flux Synchronous Motor"
order: 4
year: "ENSEEIHT – 2A (2026)"
location: "INP ENSEEIHT, Toulouse"
type: "Micro-project (design, build, test)"
summary: "Design, hand-winding, supply and testing of a three-phase self-controlled axial-flux permanent magnet motor, from the magnetic model to the prototype's nameplate."
cover:
  src: /assets/img/projects/micromag/bench.webp
  width: 593
  height: 439
  alt: "MicroMAG axial-flux motor test bench"
gallery:
  - src: /assets/img/projects/micromag/magnetic-circuit.webp
    width: 545
    height: 816
    title: "Equivalent magnetic circuit used for the design"
  - src: /assets/img/projects/micromag/winding.webp
    width: 844
    height: 983
    title: "Hand-wound three-phase stator"
  - src: /assets/img/projects/micromag/commutation.webp
    width: 1380
    height: 623
    title: "Switching sequence of the six reed switches (120° control)"
  - src: /assets/img/projects/micromag/emf.webp
    width: 658
    height: 426
    title: "Back-EMF of two phases on the oscilloscope"
  - src: /assets/img/projects/micromag/torque-speed.webp
    width: 978
    height: 560
    title: "Idealised torque–speed characteristic"
  - src: /assets/img/projects/micromag/nameplate.webp
    width: 1380
    height: 659
    title: "Nameplate of our prototype"
---

### Project Objective

Design and build a three-phase, self-controlled synchronous motor with an axial flux, using the ENSEEIHT MicroMAG kit, then compare the magnetic model with test results. Carried out in pairs with Patrice Masson, in the electromechanical conversion course.

### Approach

**1. Understand**

- Axial-flux vs radial-flux machines: here the flux crosses the air gap parallel to the shaft.
- From the magnets' field to torque: Laplace forces on the radial conductors, lever arm, and why conductors at the outer radius contribute more.

**2. Design the winding**

- Equivalent magnetic circuit (two magnets, two air gaps), Ampère's law and a linear magnet model: air-gap flux density ≈ 0.37 T.
- Number of turns for a target of 85 mN·m per phase at 2.5 A: 35 turns per phase.

**3. Build**

- Wound the three phases by hand: 30 turns per phase, two slots per pole and per phase, phases shifted by 120°.
- Checks: continuity, winding direction, free rotation, and back-EMF observed by turning the rotor by hand.

**4. Supply**

- Electromechanical inverter: six reed switches actuated by magnets on a disc linked to the rotor (self-control).
- 120° commutation (two phases conducting at a time) and adjustment of the commutation angle relative to the back-EMF.

**5. Characterise**

- Back-EMF constant ≈ 0.027 V·s/rad, 8 % below the model.
- Static torque measured with a spring balance: 182.6 mN·m with two phases supplied.
- No-load speed of 360 rpm, phase resistance and power balance at 228 rpm, then a nameplate for the prototype.
- Proposals to improve efficiency: smaller air gap, flush-mounted magnets, shorter end windings, less friction and electronic commutation.

### Skills Developed

- Magnetic circuits and permanent magnet machines.
- Sizing a winding from a torque specification.
- Hands-on prototyping: winding, wiring, commutation adjustment.
- Test methods and critical comparison between model and measurements.
