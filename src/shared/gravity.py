class Gravity():
    g_force = 1

    def __init__(self, mass):
        self.mass = mass
        self.falling_speed = Gravity.g_force

    def calculate_falling_acceleration(self):
        self.falling_speed += Gravity.g_force + self.mass

    def get_falling_speed(self):
        return self.falling_speed
