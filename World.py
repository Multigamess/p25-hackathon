import numpy as np


class Time:
    def __init__(self, second, minute, hour):
        self.second = second
        self.minute = minute
        self.hour = hour

    def add_hour(self, h):
        self.hour += h

    def add_minute(self, m):
        self.set_hour((self.minute + m)//60)
        self.minute = (self.minute + m) % 60

    def add_second(self, s):
        self.set_minute((self.second + s)//60)
        self.second = (self.second + s) % 60


class World:
    def __init__(self):
        self.size
        self.world_time = Time(0, 0, 0)
        self.map = self.generate_world()
        pass

    def generate_world(self):
        return np.random.uniform(0, 1, (self.size, self.size))

    def tick(self):
        self.world_time.add_second(1)
        pass

    def display(self):

        pass
