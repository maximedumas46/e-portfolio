---
title: "CVS Project – Power Converters"
order: 2
year: "ENSEEIHT – 2A (2026)"
location: "INP ENSEEIHT, Toulouse"
type: "Lab project (simulation + test bench)"
summary: "Four lab sessions on static converters: buck chopper, single-phase H-bridge inverter, inverter output filtering and electrothermal study, each simulated in PLECS then measured on the bench."
cover:
  src: /assets/img/projects/cvs/cover.webp
  width: 578
  height: 347
  alt: "Oscilloscope capture of the three-level H-bridge inverter"
gallery:
  - src: /assets/img/projects/cvs/buck-plecs.webp
    width: 500
    height: 170
    title: "Buck chopper and PWM modulator in PLECS"
  - src: /assets/img/projects/cvs/buck-waveforms.webp
    width: 475
    height: 330
    title: "Buck chopper: chopped voltage, output voltage and currents"
  - src: /assets/img/projects/cvs/buck-commutation.webp
    width: 534
    height: 372
    title: "IGBT turn-on: diode reverse recovery (400 ns/div)"
  - src: /assets/img/projects/cvs/buck-ratios.webp
    width: 576
    height: 272
    title: "Measured average values versus duty cycle"
  - src: /assets/img/projects/cvs/hbridge-schematic.webp
    width: 516
    height: 250
    title: "Single-phase H-bridge inverter"
  - src: /assets/img/projects/cvs/hbridge-waveforms.webp
    width: 578
    height: 347
    title: "Three-level output voltage of the H-bridge"
  - src: /assets/img/projects/cvs/fft-2-vs-3-levels.webp
    width: 360
    height: 360
    title: "Spectra: two-level vs three-level PWM"
  - src: /assets/img/projects/cvs/bode-filters.webp
    width: 341
    height: 318
    title: "Bode plot of the LC output filter (PLECS AC sweep)"
  - src: /assets/img/projects/cvs/thermal-sim.webp
    width: 360
    height: 360
    title: "Electrothermal simulation: losses and junction temperatures"
  - src: /assets/img/projects/cvs/losses.webp
    width: 805
    height: 323
    title: "Simulated losses versus frequency, voltage and current"
---

### Project Objective

Understand how a static converter turns one form of electrical energy into another, by simulating each circuit in **PLECS** and then wiring it on a lab test bench to check that measurements match the simulation. Carried out in pairs with Patrice Masson, over four sessions in autumn 2026.

### Models Studied

**1. Buck chopper (step-down DC-DC converter)**

- PWM control: a comparator between the setpoint and a carrier sets the duty cycle α.
- Simulation and measurements at E = 200 V, 8 kHz: chopped voltage, triangular inductor current (continuous conduction), smooth output voltage.
- Spectrum of the chopped voltage (harmonics at the switching frequency and its multiples) and role of the LC filter (cut-off ≈ 246 Hz).
- Observed the diode reverse recovery at each switching (≈ 100 ns edge, damped oscillations) and explained why the output stays slightly below αE under load.

**2. Single-phase H-bridge inverter**

- Two switching legs driven by opposite sinusoidal references: three-level output voltage (+E, 0, −E).
- Showed that the fundamental doubles (V1 = ma·E), the DC component cancels and the apparent switching frequency doubles (4 kHz instead of 2 kHz).
- Linear modulation up to ma = 1, then overmodulation; harmonic analysis checked on the oscilloscope FFT.

**3. Filtering the PWM inverter output**

- Second-order LC filter: where to place its natural frequency between the 50 Hz fundamental and the switching frequency.
- Compared two filters (246 Hz and 851 Hz): attenuation, phase lag at 50 Hz, inductor current ripple, size.
- Two-level vs three-level PWM: three-level control divides the current ripple by 4 for the same filter.
- Explored resonance: with the modulating signal near the filter's natural frequency, the output voltage doubled.

**4. Electrothermal study of a 3 kW buck chopper**

- Measured efficiency on the bench (η ≈ 97 % at 3 kW) with an uncertainty analysis, and the heatsink temperature rise.
- PLECS electrothermal model using the IGBT module's thermal data: conduction vs switching losses, junction temperatures.
- Showed how losses change with frequency, voltage and current, and that the inductor's winding resistance dissipates as much as all the semiconductors.

### Skills Developed

- Power electronics: DC-DC and DC-AC converters, PWM, harmonics and filtering.
- Simulation with PLECS and comparison with real measurements.
- Measurements on a power bench: oscilloscope, current probes, FFT, wattmeter, thermocouple.
- Risk analysis before wiring, and rigorous reporting with measurement uncertainties.
