#!/usr/bin/python


cadena = "esto es un ejemplo de cadena"

#Centrar una cadena en base a una longitud y relleno

print ("str.center(40, '-') : ", cadena.center(40, '-'))

#Alinea una cadena a la izquierda en base a una longitud y relleno

print ("cadena.ljust(40, '-') : ", cadena.ljust(40, '-'))

#Devuelve una cadena con 0 a la izquierda hasta completar una longitud

print ("str.zfill(40) : ", cadena.zfill(40))

#Devuelve el numero de apariciones de una subcadena dentro de una cadena

sub = "o"
print ("str.count(sub, 0, 40) : ", cadena.count(sub, 0, 40))

#Comprobamos si una cadena empieza por una determinada subcadena

print ("str.startswith('est') : ",cadena.startswith('est'))

#Devuelve una cadena sin caracteres al principio y al final

cadena="000esto es una cadena000"
print ("str.strip('0') : ",cadena.strip('0'))

#Convertir la cadena en minúsculas

cadena = "CADENA DE EJEMPLO"
print ("str.lower() : ", cadena.lower())
