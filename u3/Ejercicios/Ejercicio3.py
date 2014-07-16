ocho= 8
cuatro = 4

operacion = str(input("Introduce sumar (s), restar (r), multiplicar (m) o dividir (d): "))

if operacion == "s":
    suma = ocho + cuatro
    print("Ocho mas cuatro %i" %suma)
elif operacion == "r":
    resta = ocho - cuatro
    print("Ocho menos cuatro %i" %resta)
elif operacion == "m":
    multi = 8 * 4
    print("Ocho por cuatro %i" %multi)
elif operacion == "d":
    divi = 8 / 4
    print("Ocho dividido por cuatro %i" %divi)
else :
    print("Operación desconocida")
