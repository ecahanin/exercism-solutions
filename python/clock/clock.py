class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = (hour, minute)
        self.normalize()

    def __repr__(self):
        return f'Clock({self.hour},{self.minute})'

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        if type(self) == type(other):
            return self.hour == other.hour and self.minute == other.minute
        else:
            return False

    def __add__(self, minutes):
        new_clock = Clock(self.hour, self.minute + minutes)
        new_clock.normalize()
        return new_clock

    def __sub__(self, minutes):
        return self + (-minutes)

    def normalize(self):
        self.hour += int(self.minute/60)
        if self.minute < 0 and self.minute % 60:
            self.hour -= 1
        self.minute = self.minute % 60
        self.hour = self.hour % 24
