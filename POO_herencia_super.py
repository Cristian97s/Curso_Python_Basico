class Persona():

    def __init__(self, nombre, edad, Lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_resiedencia = Lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad,
              "Residencia: ", self.lugar_resiedencia)

class Empleado(Persona):

    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        # la funcion super esta llamando el metodo init de la clase padre
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antigüedad = antigüedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "Antigüedad: ", self.antigüedad)

Antonio = Empleado(1500, 15, "Antonio", 25, "Espana")
Antonio.descripcion()
# para saber si un objeto es instancia de una clase determinada (principio de sustitucion)
print(isinstance(Antonio, Empleado))