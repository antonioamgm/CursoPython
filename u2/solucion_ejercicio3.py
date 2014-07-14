#!/usr/bin/python

lista1 = [1, 'a', 2, 'b', 3, 'c']

#Agregar un elemento al final de la lista

lista1.append(4)
print ("Lista : ", lista1)

#Eliminar el último elemento de la lista

lista1.pop()
print ("Lista : ", lista1)

#Ordenar la lista en orden ascendente

lista1 = [1,8,4,16,78]

lista1.sort();
print ("Lista ordenada ascendentemente: ", lista1)

#Ordenar la lista en orden descendente

lista1.reverse()
print ("Lista ordenada descendentemente: ", lista1)

#Obtener el máximo valor de la lista

print ("Elemento mas grande : ", max(lista1))

#Obtener la longitud de la lista

print ("Longitud de la lista : ", len(lista1))

