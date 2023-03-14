#se crea clase persona
class Persona:
    # constructor de la clase
    def __init__(self, cedula , nombre , ocupacion): #dentro del parentesis van los atributos que van a tener la clase
        self.cedula = cedula # va a tener cedula
        self.nombre = nombre #va a tener nombre
        self.ocupacion = ocupacion #va atener ocupación

#se crea clase hija estudiante
class Estudiante(Persona): #clase hija hereda los constructores y metodos de la clase padre
 pass #
estu1=Estudiante("116730570", "Candy Cubillo"," Estduante Informática Educativa")# se crea variable estu1 que va aser igual a lo que este en clase estudiante, a esto se asigna lo que hereda de la clase
print(estu1.cedula, estu1.nombre, estu1.ocupacion) #muestra el nombre con el metodo de la herencia