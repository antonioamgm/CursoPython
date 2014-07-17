def calcularIva(cantidad, iva = 0.21):
    print(iva)
    total = cantidad * iva
    #total +=cantidad
    print("El calculo de iva es %f" %total)

valor = float(input("Introduce la cantidad: "))
impuesto = float(input("Introduce el impuesto: "))

calcularIva(valor,impuesto)
