from simulation import DroneSimulator
from controller import PIDController
import time

sim = DroneSimulator()
controller = PIDController(kp=0.8, ki=0.1, kd=0.05)

target_angle = 0.0

for i in range(100):
    current_angle = sim.get_angle()
    control = controller.update(target_angle, current_angle)
    sim.apply_control(control)

    print(f"Step {i}: Angle={current_angle:.3f}, Control={control:.3f}")
    time.sleep(0.05)
