import sqlite3 as dbapi

class Interfact(object):
    bbdd = dbapi.connect("bbdd.dat")
    def __init__(self):
        print("Clase menu cargado")

    def insertUsuario(self, *campos, **datos):
        print("Insertar")
        self.bbdd.cursor()
        self.bbdd.execute("""insert into usuario(""" + campos + """
         values ('""" + datos + """') """)
        self.bbdd.commit()
        self.bbdd.close()

    def buscarUsuario(self):
        print("Buscar")
    def borrarUsuario(self):
        print("Borrar")
    def listarUsuario(self):
        print("Lista")



