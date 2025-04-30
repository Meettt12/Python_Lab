#Identify The Shape And Get Volume Of It

import math

class RegularShape:
    def __init__(self, shape, **kwargs):
        self.shape = shape.lower()
        self.data = kwargs

    def area(self):
        if self.shape == "square":
            return self.data['side'] ** 2
        elif self.shape == "rectangle":
            return self.data['length'] * self.data['breadth']
        elif self.shape == "circle":
            return math.pi * self.data['radius'] ** 2
        elif self.shape == "triangle":
            s = (self.data['a'] + self.data['b'] + self.data['c']) / 2
            return math.sqrt(s * (s - self.data['a']) * (s - self.data['b']) * (s - self.data['c']))
        elif self.shape == "equilateral triangle":
            return (math.sqrt(3) / 4) * self.data['side'] ** 2
        else:
            return None

    def perimeter(self):
        if self.shape == "square":
            return 4 * self.data['side']
        elif self.shape == "rectangle":
            return 2 * (self.data['length'] + self.data['breadth'])
        elif self.shape == "circle":
            return 2 * math.pi * self.data['radius']
        elif self.shape == "triangle":
            return self.data['a'] + self.data['b'] + self.data['c']
        elif self.shape == "equilateral triangle":
            return 3 * self.data['side']
        else:
            return None

shape1 = RegularShape("square", side=5)
print("Area:", shape1.area())
print("Perimeter:", shape1.perimeter())

