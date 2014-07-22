class MyMetaclase3(type):
    def __new__(meta, name, bases, dct):
        print ('Creando la clase', name)
        return type.__new__(meta, name, bases, dct)
    def __init__(cls, name, bases, dct):
        print ('Inicializando la clase', name)
        type.__init__(cls, name, bases, dct)
