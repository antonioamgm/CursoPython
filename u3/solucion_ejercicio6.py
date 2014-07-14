#!/usr/bin/python

numero = 0
suma = 0

while numero < 100:
    numero += 1
    if numero % 2 != 0:
        continue
    suma += numero
    

print ("El resultado de la suma es: ", suma)