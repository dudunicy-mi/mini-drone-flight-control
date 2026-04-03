import numpy as np

class SimpleEKF:
    def __init__(self):
        # state: [angle, angular_velocity]
        self.x = np.array([[0.0], [0.0]])
        self.P = np.eye(2)

        self.Q = np.array([[0.01, 0], [0, 0.01]])  # process noise
        self.R = np.array([[0.05]])               # measurement noise

        self.F = np.array([[1, 1],
                           [0, 1]])  # state transition
        self.H = np.array([[1, 0]])  # measurement matrix

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, z):
        y = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)

        self.x = self.x + K @ y
        self.P = (np.eye(2) - K @ self.H) @ self.P

    def get_state(self):
        return self.x[0, 0]
