numero= int(input("Intruduce tu edad: "))

if numero < 0:
    print("La edad no puede ser negativa %i" %numero)
elif numero > 18:
    print("Eres mayor de de edad %i" %numero)
else:
    print("Eres menor de edad %i" %numero)
