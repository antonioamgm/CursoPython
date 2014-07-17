#!/usr/bin/python

class Empleado():

    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def impuestos(self):
        print("El nombre es:", self.nombre)
        print
        print("El sueldo es:", self.sueldo)
        print
        if self.sueldo > 800:
            print("Debe pagar impuestos.")
        else:
            print("No debe pagar impuestos.")
