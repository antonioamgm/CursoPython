#!/usr/bin/python

numero1 = 8
numero2 = 4

operacion = input("¿Qué operación deseas realizar? (sumar, restar, multiplicar, dividir): ")

if operacion == "sumar":
    resultado = numero1 + numero2
    print ("El resultado de la suma es : ", resultado)
elif operacion == "restar":
    resultado = numero1 - numero2
    print ("El resultado de la resta es : ", resultado)
elif operacion == "multiplicar":
    resultado = numero1 * numero2
    print ("El resultado de la multiplicación es : ", resultado)
elif operacion == "dividir":
    resultado = int(numero1 / numero2)
    print ("El resultado de la division es : ", resultado)
else:
    print ("Operación desconocida.")