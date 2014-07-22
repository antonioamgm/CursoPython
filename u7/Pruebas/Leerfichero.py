f = open("prueba.txt", "r+")

f.write("uno \n")
f.write("dos \n")
f.write("tres \n")
f.write("cuatro \n")
f.write("cinco \n")

while True:
    linea = f.readline()
    if not linea:
        break
    print(linea)

    
f.write("seis \n")
f.write("siete \n")

f.close()

    
