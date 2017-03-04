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

lista = ListaSimple()
vacio = lista.siVacio()
contador = 0
@app.route('/Agregar',methods=['POST'])  
def agregar():
    if vacio == True:
        parametro = str(request.form['dato'])
        identificador = str(request.form['dato2'])
        nuevo= NodoSimple(parametro, identificador)
        lista.primero = nuevo
        lista.ultimo = nuevo
        nuevo.derecha = nuevo
        return "Hola " + str(nuevo.getPalabra()) + str(nuevo.getIdentificador())+ str(contador+1)+ "!"



    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')