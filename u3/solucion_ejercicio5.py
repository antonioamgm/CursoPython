#!/usr/bin/python

import math

numero = int(input("Introduce un número: "))

while numero != 0:
    print ("El resultado de elevar el numero al cuadrado es: " , math.pow(numero,2))
    numero = int(input("Introduce un número: "))
    if numero == 0:
        break
