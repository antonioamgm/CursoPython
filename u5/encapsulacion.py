class Ejemplo:
    def publico(self):
        print("Público.")

    def __privado(self):
        print("Privado.")

ej = Ejemplo()
ej.publico()
ej.__privado()