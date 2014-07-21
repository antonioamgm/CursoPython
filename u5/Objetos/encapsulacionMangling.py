class Ejemplo:
    def publico(self):
        print("Público.")

    def __privado(self):
        print("Privado.")

ej = Ejemplo()
ej.publico()
#ej.__privado()
#utilizar una clase privada mangling
ej._Ejemplo__privado()



