#!/usr/bin/python


str = "en un lugar de la mancha"

#Convertir la primera letra de la cadena en mayúsculas

print ("str.capitalize() : ", str.capitalize())

#Convertir toda la cadena a mayúsculas

print ("str.upper() : ", str.upper())

#Alinea una cadena a la derecha en base a una longitud y relleno

print ("str.rjust(40, '=') : ", str.rjust(40, '='))

#Devuelve la posición de una subcadena dentro de la cadena

sub = "lugar"
print ("str.find(lugar) : ", str.find(sub))

#Comprobamos si una cadena finaliza por una determinada subcadena

print ("str.endswith('esto') : ",str.endswith('esto'))

#Cambia una porción de la cadena por otra subcadena

print ("str.replace('un', 'muy') : ",str.replace('un', 'muy'))