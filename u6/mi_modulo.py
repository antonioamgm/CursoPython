'''
Created on 19/06/2014

@author: JLMD
'''
class MiClase(object):
    '''
    MiClase, una clase que no hace nada, pero es mía
    '''
    def __init__(self, params):
        self.params = params
    def __str__(self):
        return "Una clase cualquiera con: " + self.params + "."
