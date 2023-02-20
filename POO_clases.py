class Coche():
    # estado inicial lo expecificamos con el constructor

    def __init__(self):

        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        # ahi que encapsular, proteger la propiedad para que no se pueda modificar con dos __
        self.__ruedas = 4
        self.__enmarcha = False

    # self hace referencia al propio objeto de perteneciencia a la clase
    # o que es lo mismo la instancia de la propia clase semejante al this en otros lenguajes
    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El Coche está en marcha"
        
        elif (self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequo, no se puede arrancar"
        
        else:
            return "El Coche está parado"

    def estado(self):
        print("El Coche tiene ", self.__ruedas, " ruedas. Un ancho de ",
              self.__ancho_chasis, " Y un largo de ", self.__largo_chasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "Cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "Cerradas"):
            return True
        else:
            return False

mi_coche = Coche()  # instancia una clase
# para acceder a propiedades y comportamiento de un objeto necesitamos la nomenclatura del .
print(mi_coche.arrancar(True))
mi_coche.estado()
#print(mi_coche.chequeo_interno()) #encapsular el metodo

# creando un objeto diferente con sus propias caracteristicas y comportamientos
print("----------A continuación creamos el segundo objeto-------------")

mi_coche2 = Coche()
print(mi_coche.arrancar(False))
# la variable ruedas esta encapsulada para python la variable ruedas y __ruedas son difertentes
# mi_coche2.__ruedas=5
mi_coche2.estado()
#print(mi_coche2.chequeo_interno()) #encapsular el metodo