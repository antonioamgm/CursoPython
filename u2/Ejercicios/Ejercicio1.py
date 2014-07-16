import math

#mostrar en pantalla e valor absoluto de -5

print("Mostrar el valor absoluto de -5: ", abs(-5))

#mostrar en pantalla la raíz cuadrada de 123

print("Mostrar lar raíz cuadrada de 123: ", math.sqrt(123))

#mostrar en pantalla el resultado de elevar 4 a la potencia de 8


print("Mostrar el resultado de elevar 4  a la pontencia de 8: ",math.pow(4, 8))

#mostrar en pantalla el resultado de redondear el numero 34.1245667 a 4

print("Mostrar lar raíz cuadrada de 123: ",math.ceil(34.1245667))

#mostrar en pantalla el resultado de convertir entero 6 a tipo float

print("Mostrar el resultado de convertir un entero 6 a float: ", 6*1.0)


#mostrar en pantalla el resultado de convertir entero 8 a tipo hexadecimal

print("Mostrar el resultado de convertir 8 tipo hexadecimal: ", hex(8))



''' comentarios en Python largos '''



print(type(input()))

edad = input("Dime tu edad:")
print("Mi edad multiplicada por tres es ", int(edad)*3)

altura = input("Dime tu altura en m: ")

altcm = float(altura) * 100

inicio ="Tu altura: "
cm = " cm."
cadena = inicio + str(altcm) + cm
print (cadena)
