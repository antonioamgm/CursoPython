#!/usr/bin/python

entrada = ""
suma = 0
fallido = 0

while suma < 3:
    suma += 1
    print ("Intento %d. " % suma)
    entrada = input("Clave: ")
    if entrada == "despedida":
        continue
    fallido += 1

print ("Tuviste %d intentos fallidos. " % fallido)
