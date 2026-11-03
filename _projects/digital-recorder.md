---
title: "SAE – Digital Recorder (Software Part)"
order: 2
year: "BUT2"
location: "BUT GEII - IUT Paul Sabatier"
type: "SAE"
summary: "Design a digital recorder capable of capturing, storing, and reproducing an audio signal."
cover:
  id: "3d2323_0b032015f9c441c2afad59dd915a9116~mv2.png"
  width: 1474
  height: 898
  fx: 0.5
  fy: 0.5
gallery: []
---

### Project Objective

Design a digital recorder capable of capturing, storing, and reproducing an audio signal.
The software part consisted of programming the STM32 peripherals (ADC, DAC, timers) and developing the different software functions to manage the recording and playback of the signal.

### Achievements

- Implementation of three main functions:
  - **Copy mode:** direct acquisition via the ADC and immediate playback via the DAC.
  - **Recording:** storage of converted values in RAM using the ADC.
  - **Playback:** reproduction of the signal at the output using the DAC and the recorded values.
- Configuration of the timers to maintain a sampling frequency of 11.025 kHz.
- Unit testing and validation with an oscilloscope and signal generator.
- Verification of compliance with the V-cycle and the project specifications.

### Skills Developed

- Embedded C programming with STM32CubeMX and HAL.
- Use of STM32 peripherals: ADC, DAC, and Timer.
- Fundamentals of digital signal processing (sampling, playback).
- Teamwork, lab notebook, and project methodology.
