#!/usr/bin/python

#Agregar varios elementos al final de una lista

lista1 = [123, 'xyz', 'zara', 'abc', 123];
lista2 = [2009, 'manni'];
lista1.extend(lista2)

print ("Lista : ", lista1)

#Agregar un nuevo elemento en una determinada posicion

lista1.insert( 3, 'nuevo elemento')
print ("Lista : ", lista1)

#Borrar un elemento de la lista

lista1.remove('abc')
print ("Lista : ", lista1)

#Contar las apariciones de un elemento en la lista

print ("Apariciones de 123 : ", lista1.count(123))

#Devolver la primera aparicion de un elemento en la lista

print ("Primera aparicion de xyz : ", lista1.index( 'xyz' ))

#Devolver el elemento mas pequeño de la lista


lista1 = [456, 700, 200]
print ("Elemento mas pequeño : ", min(lista1))