class Usuario(object):
    cont = 0
    __dni = None
    __nombre = None
    __tlfn = None
    __mail = None

    def __init__(self):
        Usuario.cont +=1

    def setDni(self, dni):
        self.__dni = dni
    def getDni(self):
        return self.__dni

    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre

    def setTlfn(self, tlfn):
        self.__tlfn = tlfn
    def getTfn(self):
        return self.__tlfn

    def setMail(self, mail):
        self.__mail = mail
    def getMail(self):
        return self.__mail


    dni = property(getDni, setDni)
    nombre = property(getNombre, setNombre)
    tlfn = property(getTfn, setTlfn)
    mail = property(getMail, setMail)


