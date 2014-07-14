#!/usr/bin/python


def crear_lista():
    ''' Almacena 5 números enteros que pide al usuario y los lista por pantalla '''
	lista = []
    
    for i in range(5):
        numero = int(input("Introduce un número: "))
        lista.append(numero)

    print("La lista creada es: ", lista)

crear_lista()