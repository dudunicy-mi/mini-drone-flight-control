from simulation import DroneSimulator
from controller import PIDController
from ekf import SimpleEKF
import time

sim = DroneSimulator()
controller = PIDController(kp=0.8, ki=0.1, kd=0.05)
ekf = SimpleEKF()

target_angle = 0.0

for i in range(100):
    measurement = sim.get_angle()

    ekf.predict()
    ekf.update([[measurement]])

    estimated_angle = ekf.get_state()

    control = controller.update(target_angle, estimated_angle)
    sim.apply_control(control)

    print(f"Step {i}: Measured={measurement:.3f}, Estimated={estimated_angle:.3f}")
    time.sleep(0.05)
