#!/usr/bin/python

diccionario = {'Nombre': 'Pedro', 'Edad': 12}

#Obtener la lista de claves y valores del diccionario

print ("Lista de claves y valores: ", diccionario.items())

#Obtener la lista de claves del diccionario

print ("Lista de claves: ", diccionario.keys())

#Obtener la lista de valores del diccionario

print ("Lista de valores: ", diccionario.values())

#Vaciar el diccionario

diccionario.clear()
print ("La longitud del diccionario es : ", len(diccionario))