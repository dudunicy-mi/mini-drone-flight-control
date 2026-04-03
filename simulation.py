import random

class DroneSimulator:
    def __init__(self):
        self.angle = random.uniform(-1, 1)

    def get_angle(self):
        noise = random.uniform(-0.02, 0.02)
        return self.angle + noise

    def apply_control(self, control):
        self.angle += control * 0.1
