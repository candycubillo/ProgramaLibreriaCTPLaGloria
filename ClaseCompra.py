# Clase Compra que guarda la información de las compras realizadas
class Compra:

    #constructor de la clase
    def __init__(self, cedula, articulo, cantidad, precioUnitario): #ATRIBUTOS DE LA CLASE
        self.cedula = cedula # SE LE ASIGNA CEDULA A CEDULA
        self.articulo = articulo #SE LE ASIGNA  A SELF.ARTICULO = ARTICULO
        self.cantidad = cantidad #CANTIDAD VA A SER IGUAL A CANTIDAD
        self.precioUnitario = precioUnitario #PERCIOUNITARIO VA HACER IGUAL A PRECIO UNITARIO

    def precio_total(self): #FUNCIÓN DEL PRECIO TOTAL PARA LOS PRODUCTOS
        return self.cantidad * self.precioUnitario #RETORNA LO QUE ESTA EN CANTIDAD Y LO MULTIPLICA POR EL PRECIOUNITARIO


