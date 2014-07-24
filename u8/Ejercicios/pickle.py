try:
    import cPickle as pickle
except ImportError:
    import pickle
    
fichero = open("datos.dat", "wb")
animales = ["piton", "mono", "camello"]
lenguajes = ["python", "mono", "perl"]
pickle.dump(animales, fichero, 0)
pickle.dump(lenguajes, fichero, 0)
fichero.close()

fichero = open("datos.dat", "rb")
animales2= pickle.load(fichero)
lenguajes2= pickle.load(fichero)
print(animales2)
print(lenguajes2)
fichero.close()   
