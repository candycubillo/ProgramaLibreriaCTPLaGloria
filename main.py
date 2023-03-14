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

# Funciones independientes
def clear(): #función limpia consola

    os.system('cls' if os.name=='nt' else 'clear') #indica que se limpia pantalla en windows

def agregar_persona(): #FUNCIÓN QUE PERMITE AGREGAR PERSONAS con la clase persona
    cedula = input("Ingrese la cédula de la persona : ") #A CEDULA EL USUARIO PODRA DIGITAR SU CEDULA
    nombre = input("Ingrese el nombre de la persona : ") #USUARIO INGRESA NOMBRE
    ocupacion = input("Ingrese la ocupación : ")         # USUARIO INGRESA SU OCUPACIÓN
    persona = Persona(cedula, nombre, ocupacion) #A LA VARIABLE PERSONA SE LE ASIGNA LOS ATRIBUTOS DE PERSONA
    personas.append(persona)                     #AGREGA DATOS DE LOS USUARIOS AL FINAL DE LA LISTA
    print("Persona agregada exitosamente.") # IMPRIME MENSAJE

def eliminar_persona():  #FUNCIÓN QUE PERMITE ELIMINAR PERSONAS con la clase persona
    encuentraP = int(0)   #VARIABLE PARA IDENTIFICAR SI EL REGISTRO EXISTE
    cedula = input("Ingrese la cédula de la persona: ")    #CAPTURA LA IDENTIFICACION DE LA PERSONA
    for i, persona in enumerate(personas):    #CICLO PARA RECORRER LA LISTA DE PERSONAS
        if persona.cedula == cedula:   #COMPARA SI LA CEDULA DIGITADA ES IGUAL A LA CEDULA DEL REGISTRO ACTUAL DE LA CLASE
            print(f"Nombre: {persona.nombre}")   #IMPRIME EL NOMBRE DE LA PERSONA PARA IDENTIFICARLA
            encuentraP = int(1)   #ASIGNA 1 A LA VARIABLE CUANDO ENCUENTRA EL REGISTRO EN LA LISTA
            personas.pop(i)   #ELIMINA EL REGISTRO QUE COINCIDE CON LA BUSQUEDA
            print("\nPersona eliminada exitosamente.")   #MENSAJE DE CONFIRMACION DEL BORRADO

    if encuentraP == 0:   #VALIDA SI LA VARIABLE ESTA EN CERO, QUIERE DECIR QUE NO ENCONTRÓ EL REGISTRO
            print("\nNo existen datos para esa persona")   #MENSAJE DE INFORMACION QUE LA PERSONA NO EXISTE EN LA LISTA

def modificar_persona():   #FUNCIÓN QUE PERMITE MODIFICAR PERSONAS con la clase persona
    encuentraP = int(0)   #VARIABLE PARA IDENTIFICAR SI EL REGISTRO EXISTE
    cedula = input("Ingrese la cédula de la persona: ")    #CAPTURA LA IDENTIFICACION DE LA PERSONA
    for i, persona in enumerate(personas):    #CICLO PARA RECORRER LA LISTA DE PERSONAS
        if persona.cedula == cedula:   #COMPARA SI LA CEDULA DIGITADA ES IGUAL A LA CEDULA DEL REGISTRO ACTUAL DE LA CLASE
            encuentraP = int(1)   #ASIGNA 1 A LA VARIABLE CUANDO ENCUENTRA EL REGISTRO EN LA LISTA
            nombreM = input("Ingrese nuevo nombre de la persona: ")   #CAPTURA EL NUEVO NOMBRE DE LA PERSONA
            ocupacionM = input("Ingrese nueva ocupación: ")   #CAPTURA LA NUEVA OCUPACION DE LA PERSONA
            persona.nombre = nombreM   #MODIFICA EL NOMBRE DE LA LISTA CON EL NUEVO NOMBRE INGRESADO
            persona.ocupacion = ocupacionM   #MODIFICA LA OCUPACION DE LA LISTA CON LA NUEVA OCUPACION INGRESADA
            print("\nPersona modificada exitosamente.")   #MENSAJE DE CONFIRMACION DE LA MODIFICACION

    if encuentraP == 0:   #VALIDA SI LA VARIABLE ESTA EN CERO, QUIERE DECIR QUE NO ENCONTRÓ EL REGISTRO
            print("\nNo existen datos para esa persona")   #MENSAJE DE INFORMACION QUE LA PERSONA NO EXISTE EN LA LISTA

def agregar_compra():                       #FUNCION PARA AGREGAR COMPRA
    encontrado = int(0)             # BUSCA EL USUARIO EN LA LISTA
    nombrecliente = ""               # MUESTRA EL NOMBRE DEL CLIENTE ENCONTRADO
    cedula = input("Ingrese cédula del cliente : ")  #MUESTRA LA CEDULA DEL CLIENTE
    for i, persona in enumerate(personas): # CLICO FOR PARA RECORRER LA LISTA Y LAS ENUMERA CON LA CLASE PERSONAS
        if persona.cedula == cedula: # CICLO IF QUE LO QUE HAY EN PERSONA.CEDULA SE GUARDARA EN CEDULA
                encontrado = int(1) #devuelve DATOS DEL CLIENTE
                nombrecliente = persona.nombre # LLAMA LA VARIABLE NOMBRE CLIENTE Y LO IGUALA PARA QUE SE GUARDE EN PERSONA.NOMBRE


    if encontrado == 1: #dentro de la condición if si es igual a 1
        print(f"Nombre del cliente : {nombrecliente}") #va a mostrar nombre del cliente y llama función de nombre cliente
        articulo = input("Ingrese el nombre del artículo : ") #el usuario agrega el nombre del articulo que desea comprar
        cantidad = int(input("Ingrese la cantidad de unidades : ")) #el usuario ingresa cuantas unidades de articulo desea
        precioUnitario = float(input("Ingrese el precio unitario : ")) #el precio unitario del producto que el precio es float
        compra = Compra(cedula, articulo, cantidad, precioUnitario) #la variable compra, se almacena la cedula, el articulo la cantidad y el precio unitario
        compras.append(compra) #se agrega la compra al final
        print("Compra agregada exitosamente.")# muestra mensaje de compra agregada
    else: #sino
        print("Cliente no está registrado") # muestra mensaje que el cliente no esta registrado

def calcular_subtotal(): #función para calcular el subtotal de la compra
    global subtotal #subtotal es una variable global
    subtotal = sum([compra.precio_total() for compra in compras]) # el subtotal vector para almacenar la compra

def calcular_descuento(): #función calcular el descuento al cliente
    global descuento_total # descuento_total es una variable global
    if subtotal > 500: #si la compra es mayor a 500 colones
        descuento_total = subtotal * DESCUENTO / 3 # entonces el descuento_total va aser igual a subtotal por el descuento dividido entre 3

def calcular_iva(): #funcion que calcula el iva
    global iva_total #la variable iva_total es global
    iva_total = (subtotal - descuento_total) * IVA #el iva_total va a ser igual al subtotal menos descuento_total por el iva

def calcular_total(): #función que calcula total
    global total #total es una variable global
    total = subtotal - descuento_total + iva_total#total va a ser igual a subtotal menos descuento_total mas el iva_total

def mostrar_compras(): #funcion para mostrar compra
    if not compras: #sino hay compras
        print("No hay compras registradas.") # muestra mensaje que no hay compras registradas
    else: #sino
        print("Compras realizadas:") #muestra mensaje de compra realizada
        for i, compra in enumerate(compras): #recorre vector de compras
            print(f"{i+1}. {compra.articulo}: {compra.cantidad} unidades a {compra.precioUnitario} cada una, totalizando {compra.precio_total()}")
        print(f"Subtotal: {subtotal}") #imprime subtotal que esta en variable subtotal
        print(f"Descuento: {descuento_total}") #imprime descuento que esta en variable descuento_total
        print(f"Impuesto: {iva_total}") #imprime impuesto, que se almacena en variable iva_total
        print(f"Total a pagar: {total}") #imprime mensaje del total de compra que se almacena en variable total

def mostrar_compras_clientes(): #esta función se guarda en una matriz llamada matriz personas
    if not compras:#sino hay compras
        print("No hay compras registradas.")# muetra mensaje que no hay compras registradas

    else: #sino
        for i, persona in enumerate(personas): #recorre matriz en la fila personas
            comencontrada = int(0)#variable comencontrada  para buscar la persona
            print(f"\nCliente: {persona.cedula} {persona.nombre}")#imprime nombre del cliente, llama a las variables persona.cedula y persona.nombre para mostrar
            print("Compras realizadas:") #imprime mensaje de compras realizadas
            for j, compra in enumerate(compras): #recorre la matriz en columna
                if persona.cedula == compra.cedula: # si la persona se registro encuentra la cedula y la compras
                    comencontrada = int(1) # cuando encuentra la persona se asignar un 1 para que no la vuelva a buscar
                    print(f"{j + 1}. {compra.articulo} \n   Cantidad: {compra.cantidad} unidades \n   Precio unitario: {compra.precioUnitario} \n   Total: {compra.precio_total()}") #imprime en la matriz los datos guardados en ella
            if comencontrada == int(0): #si la variable comencontrada no ha realizado compras
                print("Cliente no tiene compras registradas")#muestra mensaje que el cliente no tiene compras registradas

def mostrar_personas(): # función para mostrar personas
    if not personas: # sino hay personas registradas
        print("No hay personas registradas.") # muestra un mensaje que no hay personas registradas
    else: # en este caso si la persona se agrega entonces
        print("Personas registradas:") #muestra mensaje que se registro la persona
        for i, persona in enumerate(personas): #recorre vector personas para ver si esta o no registrada la persona
            print(
                f"{i + 1}. Cédula {persona.cedula} Nombre {persona.nombre} Ocupación {persona.ocupacion}") # muestra la cedula, nombre y ocupación de la persona que se almacena en vector

def mostrar_menu_mant():
    #menú mantenimiento de personas (eliminar y modificar)
    while True:
        print("\n############## Menú mantenimiento Personas ##############")
        print("0. Eliminar datos de persona") #Eliminar una persona
        print("1. Modificar datos de persona") #Modificar los datos de una persona
        print("2. Salir") #Salir y volver al menú principal
        print("#########################################################")
        opcionmenu = input("Ingrese una opción: ") #Opción que el usuario selecciona

        if opcionmenu == "0":  #Si la opción es 0 es para eliminar una persona
            eliminar_persona()  #Llamada al método para eliminar una persona
        elif opcionmenu == "1":  #Si la opción es 1 es para modificar datos de una persona
            modificar_persona()  #Llamada al método para modificar datos de una persona
        elif opcionmenu == "2":  #Si la opción es 2 regresa al menú principal
            break  #el break se utiliza cerrar un bucle cuando se ejecuta una instrucción diferente, en este caso regresa al menú principal
        else:    # si elige opción que no este en el menu le muestra opción invalida
            print("#####  Opción inválida.  ######")    #imprime mensaje opción invalida

nomNegocio = NombreNegocio() #instancia del sigleton
nomNegocio.nombre = " ###### Librería del CTP La Gloria ######" # nombre del programa
clear()
# Menú de opciones para el usuario que visita la libreria

while True:

    print("\n", nomNegocio) #imprime nombre del negocio
    print("#########################################################")
    print("0. Agregar persona")   # la opción 0  mensaje para agregar persona
    print("1. Mostrar personas")  # la opción 1  mensaje para mostrar persona
    print("2. Agregar compra")  # la opción 2 mensaje para agregar compra
    print("3. Mostrar compras") # la opción 3 mensaje para mostrar compra
    print("4. Mostrar compras por cliente :")  # la opción 4 mensaje para mostrar compras por cliente
    print("5. Mantenimiento de personas :")  # la opción 5 mensaje para mantenimiento de personas
    print("6. Salir") # la opción 6 mensaje para salir del menu
    print("#########################################################")
    opcion = input( "Ingrese una opción : " ) # opción para que el usuario pueda elegir la opción que desea
    os.system("cls")
    if opcion == "0": # dentro de la condición si la opción es 0
        agregar_persona() #se va a agregar personas
    elif opcion == "1": #si la opción es 1
        mostrar_personas() # se va a mostrar las personas
    elif opcion == "2": #si la opción es 2
        agregar_compra() #se agrega compra
        calcular_subtotal() #se calcula el subtotal
        calcular_descuento() #se calcula descuento
        calcular_iva() #se calcula iva
        calcular_total() #se calcula el total de la compra
    elif opcion == "3":  #si la opción es 3
        mostrar_compras() #se muestran las compras
    elif opcion == "4":  #si la opción es 4
        mostrar_compras_clientes()  #se muestran las compras de cada cliente
    elif opcion == "5":  #si la opción es 5
        mostrar_menu_mant()  #se muestran el menú de mantenimiento de personas
    elif opcion == "6": #si la opción es 6 sale del programa
        break #el break se utiliza cerrar un bucle cuando se ejecuta una instrucción diferente, en este caso cierra el programa
    else:                     # si elige opción que no este en el menu le muestra opción invalida
        print("#####  Opción inválida.  ######") #imprime mensaje opción invalida