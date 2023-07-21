from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise Exception("Denominator cannot be zero")
        self.numer = numer
        self.denom = denom
        self.reduce()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)

    def __abs__(self):
        if self.numer < 0:
            return Rational(self.numer * -1, self.denom)
        else:
            return self

    def __pow__(self, power):
        if power > 0:
            return Rational(self.numer**power, self.denom**power)
        elif power < 0:
            return Rational(self.denom, self.abs_int(self.numer))**(-1*power)
        else: 
            return Rational(1,1)

    def __rpow__(self, base):
        return base **(self.numer/self.denom)

    def reduce(self):
        if self.numer == 0:
            self.denom = 1
            return True
        gcd = 1
        for i in range(1,self.abs_int(self.numer)+1):
            if not self.numer % i and not self.denom % i:
                gcd = i
        self.numer = int(self.numer/gcd)
        self.denom = int(self.denom/gcd)
        if (self.numer < 0 and self.denom < 0) or (self.numer > 0 and self.denom < 0):
            self.numer *= -1
            self.denom *= -1

    def abs_int(self, num):
        if num < 0:
            num *= -1
        return num
