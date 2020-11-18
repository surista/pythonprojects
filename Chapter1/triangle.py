#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

def  tri(base, height):
    if (base or height) < 0:
        raise ValueError("Measurements must be greater than 0")
    return 0.5 * base * height

print(tri(3,5))
