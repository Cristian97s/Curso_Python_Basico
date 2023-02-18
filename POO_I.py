class Coche():
    largo_chasis=250
    ancho_chasis=120
    ruedas=4
    enmarcha=False

    # self hace referencia al propio objeto de perteneciencia a la clase 
    # o que es lo mismo la instancia de la propia clase semejante al this en otros lenguajes
    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

mi_coche=Coche() #instancia una clase 

# para acceder a propiedades y comportamiento de un objeto necesitamos la nomenclatura del .
print("El largo del coche es:",mi_coche.largo_chasis)
print("El coche tiene", mi_coche.ruedas, "ruedas")
mi_coche.arrancar()

print(mi_coche.estado())