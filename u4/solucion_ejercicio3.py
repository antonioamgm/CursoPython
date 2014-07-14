#!/usr/bin/python


def calcular_operaciones(*numeros):
    suma = 0
    multiplicacion = 1

    for num in numeros: 
        suma += num
        multiplicacion *= num

    print("El resultado de la suma es: ", suma)
    print("El resultado de la multiplicación es: ", multiplicacion)

calcular_operaciones(105,12,34,23)
calcular_operaciones(123,23)