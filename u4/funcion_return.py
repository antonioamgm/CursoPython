#!/usr/bin/python

import math

def superficie_circulo(radio):
    superficie = math.pi * radio ** 2
    return superficie

circulo = superficie_circulo(12)
print(circulo)
