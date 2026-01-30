import numpy as np
import random as rd


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