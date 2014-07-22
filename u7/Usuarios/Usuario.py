class Usuario(object):
    def __init__(self, nombre, tlfn, mail):
        self.nombre = nombre
        self.tlfn = tlfn
        self.mail = mail
        print("Usuario %s, telefono %s, mail %s" % (self.nombre, self.tlfn, self.mail))
