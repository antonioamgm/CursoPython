class MiError(Exception): 
    def __init__(self, valor): 
        self.valor = valor
    def __str__(self): 
        return "Error " + str(self.valor)

resultado = 45

try:
    if resultado > 20:
        raise MiError(resultado)
except MiError as e:
    print(str(e))