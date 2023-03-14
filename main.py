#Libreria del CTP La Gloria
import os
from ClasePersona import Persona #se importa la clase persona
from ClaseCompra import Compra #se importa la clase compra
# Constantes
IVA = 0.15  # Impuesto al valor agregado
DESCUENTO = 0.10  # Descuento por compras mayores a $500

# Variables
matriz_personas = [] #se almacena en matriz las personas que comprarón
compras = []  # Lista de compras realizadas se almacena en vector
personas = []  # Lista de personas
subtotal = 0  # Subtotal de todas las compras realizadas
descuento_total = 0  # Descuento total aplicado a las compras
iva_total = 0  # Impuesto total a pagar
total = 0  # Total a pagar

# clase singleton para el nombre del negocio se usa una unica vez
class NombreNegocio(object):

    class __NombreNegocio : #se crea la clase nombre negocio y solo va a tener una unica instancia en el programa
      #constructor de la clase
        def __init__(self):
           self.nombre = None # variable nombre vacia

        def __str__(self): # el str para que está siempre en la misma posición de memoria
            return self.nombre # regresa lo almacenado en nombre

    instance = None #no tiene valor

    def __new__(cls):# se crea la instancia
         if not NombreNegocio.instance: # sino recibe parametro
           NombreNegocio.instance = NombreNegocio.__NombreNegocio() # la variable NombreNegocio. instancia va aser igual al NombreNegocio
         return NombreNegocio.instance #retorna el nombre con la instancia

    def __getattr__(self, nombre): #los getters  que llaman a la instancia.
         return getattr(self.instance, nombre) #devuelve lo almacenado en la instancia

    def __setattr__(self, nombre, valor): # los __setattr__ que llaman a la instancia.
        return setattr(self.instance, nombre, valor) ##devuelve lo almacenado en la instancia
