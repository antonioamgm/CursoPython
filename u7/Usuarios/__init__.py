'''
Created on 24/07/2014

@author: thinktic
'''
import Interfact

salir = True;
while salir:
    print("Que desea hacer:")
    print(" Inserta(i) \n Busca(b) \n Borra(d) \n Lista(l) \n Salir(s)")
    menu = input("i,b,d,l,s: ")
    if (menu == "i"):
        Interfact.insertUsuario()
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




