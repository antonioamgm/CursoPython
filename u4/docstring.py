'''
Created on 13/06/2014

@author: JLM
'''
def f1(param1, param2):
    '''Esta función imprime los dos valores pasados como parámetros'''
    print(param1)
    print(param2)
    print(__doc__)


f1("hola", "dos")
print(f1.__doc__)
