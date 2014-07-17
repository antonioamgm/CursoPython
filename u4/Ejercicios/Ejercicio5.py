
def crearLista(numero1, numero2):
    lis = []
    if (numero1 > 0) and (numero2 > 0):
        for i in range(numero1,numero2):
            lis.append(int(input("Introduce un numero entero: ")))
    else:
        print("El numero de rango debe ser positivo i%" %numero)  
    print(lis)
                   
crearLista(int(input("Introduce el rango de la lista: ")),int(input("Introduce el rango de la lista: ")))
