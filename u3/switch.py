#!/bin/env python
# -*- coding: utf8 -*-

import random

def spam():
    print('spam')

def ham():
    print('ham')

def egg():
    print('egg')

def unknown():
    print('unknown')

foo = random.choice(['a', 'b', 'c', 'x'])

# Primer metodo, el clásico
print("Primer metodo: "),

if foo == 'a':
    spam()
elif foo == 'b':
    ham()
elif foo == 'c':
    egg()
else:
    unknown()

# Segundo metodo, el más eficiente. Se puede prescindir de
# capturar la excepción si conocemos todas las opciones posibles
print("Segundo metodo: "),

try:
    ({'a':spam, 'b':ham, 'c':egg}[foo])()
except KeyError:
    unknown()

# Otra variante del segundo metodo
print("Segundo metodo, otra variante: "),

options = {'a':spam, 'b':ham, 'c':egg}
options.get(foo, unknown)()

# Tercer metodo, más pythonico, solo valido para dos opciones
print("Si solo hay dos opciones: "),

spam() if foo == 'a' else ham()