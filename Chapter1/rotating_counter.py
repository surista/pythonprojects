#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

class RotatingCounter:
    def __init__(self, counter = 0):
        self.counter = counter

    def increment(self):
        if self.counter == 9:
            self.counter = 0
        else:
            self.counter += 1

    def reset(self):
        a =  counter
        counter = 0
        return a


a = RotatingCounter

print(a)