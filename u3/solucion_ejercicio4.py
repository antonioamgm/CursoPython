#!/usr/bin/python

minimo = int(input("Introduce el valor mínimo: "))
maximo = int(input("Introduce el valor máximo: "))

numero = int(input("Introduce un número: "))

suma = 0

while numero > minimo and numero < maximo:
    suma+=numero
    numero = int(input("Introduce un número: "))

print ("El resultado de la suma es: " , suma)