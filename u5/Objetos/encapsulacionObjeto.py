class Encapsulation(object):
    def __init__(self,a,b,c):
        self.public = a
        self._protected = b
        self.__private = c
        
x = Encapsulation(11, 13, 17)

print(x.public)

print(x._Encapsulation__private)


