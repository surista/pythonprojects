#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self,newValue):
        if newValue >= 0:
            self.__radius = newValue
        else: raise ValueError("Value must be positive")

    def Area(self):
        return 3.14159 * (self.__radius**2)


class Circle2:
    def __init__(self, radius):
        self.radius = radius

    def setRadius(self, newValue):
        if newValue >= 0:
            self.radius = newValue
        else: raise ValueError("Value must be greater than zero")

    def Area(self):
        return 3.14159 * (self.radius ** 2)

a = Circle(3)
b = Circle2(3)

a.setRadius(5)
b.setRadius(5)

# print(a.radius)
print(b.radius)

