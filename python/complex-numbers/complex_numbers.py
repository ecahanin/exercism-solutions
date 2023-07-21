from math import cos, e, sin

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) / \
            (other.real ** 2 + other.imaginary **2)
        imaginary = (self.imaginary * other.real - self.real * other.imaginary)\
             / (other.real ** 2 + other.imaginary **2)
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2)**0.5

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        return ComplexNumber(e ** self.real, 0) * ComplexNumber(cos(self.imaginary), sin(self.imaginary))
        
