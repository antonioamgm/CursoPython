mi = int(input("Introduce un valor mínimo: "))
         
ma = int(input("Introduce un valor máximo: "))
         
numero = int(input("Introduce un número: "))

suma = 0

while numero > mi and numero < ma:
    numero = int(input("Introduce un número para sumar: "))
    suma += numero
    print("La suma es %i" %suma)
    

