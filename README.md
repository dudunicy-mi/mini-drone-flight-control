# mini-drone-flight-control
A minimal drone flight control simulation including PID-based stabilization, sensor noise modeling and closed-loop control. Inspired by PX4 and ArduPilot. Designed for learning and experimentation in UAV control systems.
- EKF-based state estimation (sensor fusion)
- Separation of measurement vs estimated state
- ## Advanced Topics

This project now includes a simple Extended Kalman Filter (EKF) for state estimation.

This mimics a core component in real-world UAV systems:
- combining noisy sensor inputs
- estimating true system state
- improving control stability
