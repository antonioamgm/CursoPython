import sqlite3 as dbapi
import Usuario

class Interfact(object):
    bbdd = dbapi.connect("bbdd.dat")
    def __init__(self):
        print("Clase menu cargado")


    def insertUsuario(self):
        Usuario.dni = input((print("Introduce dni: ")))
        Usuario.nombre = input((print("Introduce nombre: ")))
        Usuario.tlfn = input((print("Introduce teléfono: ")))
        Usuario.mail = input((print("Introduce mail: ")))
        return (Usuario.dni +', '+ Usuario.nombre + ', ' + Usuario.tlfn + ', ' + Usuario.mail)
#         self.bbdd.cursor()
#         self.bbdd.execute("""insert into usuario(""" + campos + """
#          values ('""" + datos + """') """)
#         self.bbdd.commit()
#         self.bbdd.close()

    def buscarUsuario(self):
        print("Buscar")

    def borrarUsuario(self):
        print("Borrar")

    def listarUsuario(self):
        print("Lista")



