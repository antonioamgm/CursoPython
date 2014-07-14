valor = 1

def mi_funcion():
    # Imprimirá "1", puesto que encontrará la variable
    # valor (definida a nivel de módulo)
    print(valor)

def mi_segunda_funcion():
    # Al definir la variable "valor" en la función,
    # será esta la que será tratada (no usará
    # la definida a nivel de módulo)
    valor = 5
    print(valor)

def mi_otra_funcion():
    # Lanzará un error. Como detecta que luego es modificada
    # y no se puede modificar una variable externa a la función
    # (tal y como está el código) entiende que es una variable
    # local (y peta porque no se puede hacer un print de una
    # variable no definida
    print(valor)
    valor = 10

def mi_ultima_funcion():
    # "global valor" enlaza la variable de módulo "valor".
    # Ahora, desde dentro de la función ya se puede leer
    # y ESCRIBIR en la variable de módulo "valor"
    global valor
    print(valor)
    
mi_funcion()
mi_segunda_funcion()
mi_otra_funcion()
mi_ultima_funcion()