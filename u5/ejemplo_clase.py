#!/usr/bin/python

class Empleado:
    ''' Clase base común a todos los empleados '''
    empCont = 0

    def __init__(self, nombre, salario):
        '''Inicialización del empleado'''
        self.nombre = nombre
        self.salario = salario
        Empleado.empCont += 1

    def mostrarContador(self):
        '''Mostrar el número de empleados'''
        print("Número total de empleados %d" % Empleado.empCont)

    def mostrarEmpleado(self):
        '''Mostrar los datos del empleado'''
        print("Nombre: ", self.nombre, "- Salario: ", self.salario)

Pedro = Empleado("Pedro", 22000)
Juan = Empleado("Juan", 20000)
Pedro.mostrarContador()
Pedro.mostrarEmpleado()
