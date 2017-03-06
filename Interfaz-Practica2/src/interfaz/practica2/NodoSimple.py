

if __name__ == "__main__":
    print "Hello World"

class NodoSimple (object):
    
    def __init__(self, dato=None, derecha = None):
        self.dato = dato
        self.derecha = derecha
    def __str__(self):
        return str(self.dato)


    