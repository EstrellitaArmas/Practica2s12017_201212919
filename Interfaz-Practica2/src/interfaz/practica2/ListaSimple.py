__author__ = "estre"
#Si mientras trabajan en Python alguna vez les arroja un "IndentationError" es porque en alguna linea, los tabs al inicio de la sentencia estan erroneos, por ejemplo:
#Esto es valido:
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#		self.password = password
#Esto NO es valido y arroja un "IndentationError":
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#	   self.password = password
#	   ^
#	   Esto no deberia de estar ahi, sino que tiene que estar igual de indentado que las demas sentencias.
#
#
#Recomiendo Sublime Text como IDE
#
from NodoSimple import NodoSimple 

from flask import Flask, request, Response
app = Flask("ListaSimple")
#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
class ListaSimple():
    def __init__(self):
        self.primero= None
        self.ultimo= None
    
    
    def siVacio(self):
        if self.primero == None:
            print("The left node is None/Null.")
            return True
        else:
            return False

    def verlista(self,NodoSimple):
        nodos= ""
        while NodoSimple:
            # muestra el dato
#            nodos + NodoSimple.dato
            nodos = nodos + NodoSimple.dato
            # ahora nodo apunta a nodo.prox
            NodoSimple = NodoSimple.derecha
        return nodos 
    
    def insertar(self,dato):
        if vacio == True:
            nuevo=NodoSimple(dato,None)
            vacio = False
#        else:
#            nuevo=NodoSimple(dato,NodoSimple.derecha)
            return dato
    
    
lista = ListaSimple()
vacio = lista.siVacio()
contador = 0
@app.route('/Agregar',methods=['POST'])  
def agregar():
    if vacio == True:
#        v3=NodoSimple(request.form['dato'])
#        v2=NodoSimple("Peras", v3)
#        v1=NodoSimple("Manzanas", v2)
        imprimor = lista.insertar(request.form['dato'])
#        
#        parametro = str(request.form['dato'])
#        identificador = str(request.form['dato2'])
#        nuevo= NodoSimple(parametro, identificador)
#        lista.primero = nuevo
#        lista.ultimo = nuevo
#        nuevo.derecha = nuevo
        return   str(imprimor)
#        + str(nuevo.getPalabra()) + str(nuevo.getIdentificador())+ str(contador+1)+ "!"



    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')