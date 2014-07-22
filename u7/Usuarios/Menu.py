
class Menu(object):
    def __init__(self, nombre):
        print("Clase %s cargada" %nombre)
        self.seleccionaMenu()
        #return object

    def seleccionaMenu(self):
        #menu = input("Que desea hacer: ")
        self.salir = True;
        print("Que desea hacer:")
        print(" Inserta(i) \n Busca(b) \n Borra(d) \n Lista(l) \n Salir(s)")
        menu = input("i,b,d,l,s: ")
        if (menu == "i"):
            self.insertUsuario()
        elif(menu == "b"):
            self.buscarUsuario()
        elif(menu == "d"):
            self.borrarUsuario()
        elif(menu == "l"):
            self.listarUsuario()
        elif(menu == "s"):
            self.salir = False
        else:
            print("Operacion desconocida")
        #ejecuta la clase mientras no diga salir
        while  self.salir:
            self.seleccionaMenu()

    def insertUsuario(self):
        print("Insertar")
    def buscarUsuario(self):
        print("Buscar")
    def borrarUsuario(self):
        print("Borrar")
    def listarUsuario(self):
        print("Lista")
