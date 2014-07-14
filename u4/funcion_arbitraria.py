#!/usr/bin/python

def promedio(*muestra):
    print ("La muestra es: ")
    print (muestra)
    n = len(muestra)
    print ("Hay %d elementos en la muestra " % n)
    media = float(sum(muestra)) / n
    print ("El promedio es: ", media)


promedio(1, 2, 3, 4, 5, 6, 7)
print()
promedio(14.5, 12.7, 33.6, 54, 78, 94.12)