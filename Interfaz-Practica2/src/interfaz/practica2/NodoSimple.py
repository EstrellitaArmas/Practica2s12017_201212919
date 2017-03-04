

if __name__ == "__main__":
    print "Hello World"

class NodoSimple (Object):
    
    def __init__(self, dato=None, derecha = None):
        self.dato = dato
        self.derecha = derecha
    def __str__(self):
        return str(self.dato)


    
    def getPalabra(self):
        return self.palabra
    
    def getIdentificador(self):
        return self.identificador
    
    def setPalabra(self, palabra):
        self.palabra=palabra
        
    def setIdentificador(self, identificador):
        self.identificador= identificador