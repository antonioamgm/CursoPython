'''
Created on 24/07/2014

@author: thinktic
'''
from u7.Usuarios.Interfact import *


#usuario = {"dni":None, "nombre":None, "tlfn":None, "mail":None}

user = Usuario()

salir = True;
while salir:
    print("Que desea hacer:")
    print(" Inserta(i) \n Busca(b) \n Borra(d) \n Lista(l) \n Salir(s)")
    menu = input("i,b,d,l,s: ")
    if (menu == "i"):
        user.dni = input("dni: ")
        user.nombre = input("nombre: ")
        user.tlfno = input("teléfono: ")
        user.mail = input("mail: ")
        user.cont += 1
        Interfact.insertUsuario(user)
    elif(menu == "b"):
        Interfact.buscarUsuario()
    elif(menu == "d"):
        Interfact.borrarUsuario()
    elif(menu == "l"):
        Interfact.listarUsuario()
    elif(menu == "s"):
        salir = False
    else:
        print("Operacion desconocida")




