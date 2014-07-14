#!/usr/bin/python

diccionario = {'Nombre': 'Pepe', 'Edad': 27}

#Obtener la longitud del diccionario

print ("Longitud del diccionario: ", len(diccionario))

#Obtener una copia de un diccionario

diccionario2 = diccionario.copy()
print ("La copia del diccionario es: ", diccionario2)

#Obtener el valor de una clave

print ("Valor de la clave edad: ", diccionario.get("Edad"))

#Concatenar un diccionario con otro

diccionario2 = {'Poblacion': 'Logroño'}
diccionario.update(diccionario2)
print ("El valor de diccionario es: ", diccionario)

#Borra un diccionario
diccionario.clear()
print ("El valor de diccionario es: ", diccionario)