class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
        
class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

# mi_vehiculo=Moto()
# mi_vehiculo.desplazamiento()

#polimorfismo
def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

mi_vehiculo=Camion()
desplazamiento_vehiculo(mi_vehiculo)