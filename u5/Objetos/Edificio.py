class Edificio(object):
    def __new__(cls, nombre, *alturas, **viviendas):
        print("Creación del edificio %s" %nombre)
        return object
    def __init__(self, nombre, *alturas, **viviendas):
        print("Inicializando la clase", nombre)

        
              
              

