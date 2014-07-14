#!/usr/bin/python

numero = int(input("Escriba un número entero mayor que cero: "))

if numero <= 0:
    print("'El número tiene que ser mayor que cero.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i 
    print("El factorial de", numero, "es", factorial) 	