---
title: "SAE IE – Obstacle Detection Turret"
order: 3
year: "BUT2"
location: "BUT GEII - IUT Paul Sabatier"
type: "SAE"
summary: "Design an obstacle detection turret using the PCA9685 component (16-channel PWM driver)."
cover:
  id: "3d2323_2d6b8c8874d24373b44a7c3903ae0aaa~mv2.jpg"
  width: 2718
  height: 2036
  fx: 0.5104166666666666
  fy: 0.6069767441860465
gallery: []
---

### Project Objective

Design an obstacle detection turret using the PCA9685 component (16-channel PWM driver).
The goal was to develop the control software functions to initialize the component, configure its registers, and generate PWM signals to control the turret.

### Achievements

- Studied the PCA9685 datasheet and defined functional requirements.
- Developed in Arduino (C/C++):
  - Initialization function with prescaler configuration to generate a 50 Hz frequency.
  - Function to configure a duty cycle on an LED/PWM output.
- Validated through unit testing and oscilloscope measurements (PWM signals at 0%, 60%, and 100%).
- Followed the V-model development cycle and maintained a complete lab notebook.

### Skills Developed

- Low-level programming in C/C++ (Arduino).
- I²C communication with an external component (PCA9685).
- Signal analysis and validation with an oscilloscope.
- Project methodology (V-cycle, lab notebook, unit testing).
