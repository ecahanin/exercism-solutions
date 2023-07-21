from string import ascii_uppercase, digits
from random import choice


class Robot:
    used_names = set()

    def __init__(self):
        self.reset()

    def reset(self):
        self.get_name()

    def get_name(self):
        name = ''
        for _ in range(0,2):
            name += choice(ascii_uppercase)
        for _ in range(0,3):
            name += choice(digits)
        if name in Robot.used_names:
            self.get_name()
        else:
            Robot.used_names.add(name)
            self.name = name