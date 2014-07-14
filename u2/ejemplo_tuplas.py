#!/usr/bin/python

tupla = (1, 50, 23, 56, 23)

#Obtener la posición en la que aparece un elemento

print ("Posicion del elemento 56: ", tupla.index(56))

#Averiguar el número de veces que aparece un elemento

print ("Veces que aparece el elemento 23: ", tupla.count(23))

#Obtener la longitud de la tupla

print ("Longitud de la tupla: ", len(tupla))

#Obtener el elemento mayor de la tupla

print ("Elemento mas grande : ", max(tupla))

#Obtener el elemento menor de la tupla

print ("Elemento mas pequeño : ", min(tupla))

#Convertir una lista en una tupla

lista = ['a', 'b', 'c']
tupla = tuple(lista)
print ("Elementos de la tupla : ", tupla)
