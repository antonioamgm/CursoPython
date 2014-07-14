#!/usr/bin/python

entrada = ""
suma = 0

while suma < 3 and entrada != "despedida":
    entrada = input("Clave:")
    if entrada == "despedida":
        break
    suma = suma + 1
    print ("Intento %d. \n " % suma)

print ("Tuviste %d intentos fallidos. " % suma)