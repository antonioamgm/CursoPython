def calcular(importe, descuento):
    return importe - (importe * descuento/100)

datos = [1500,10]

print(calcular(*datos))

datos2 = {"descuento":10, "importe": 1500}

print(calcular(**datos2))
