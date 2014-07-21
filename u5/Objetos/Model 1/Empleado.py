#
class Empleado:    
    __nombre = 0
    assert(type(__nombre)==String)
    __sueldo = 0
    assert(type(__sueldo)==Real)
    __impuesto = False
    assert(type(__impuesto)==Boolean)
    __contEmpleado
    assert(type(

    def __ini__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo
        if self.__sueldo > 800:
            self.__impuesto = True
        
        


    #Devuelve el nombre y el sueldo del empleado
    def publicmostraNomSueldo (self):
        
        # implementation

