class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)

# Heredamos la clase vehiculos en moto
class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    #sobreescritorio de metodo
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena, "\n", self.hcaballito)

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    
    def Carga_electrica(self):
        self.cargando=True

mi_moto = Moto("Honda", "CBR")
mi_moto.caballito()
mi_moto.estado()
mi_furgoneta=Furgoneta("Renault", "Kango")
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print(mi_furgoneta.carga(True))

#Herencia multiple
class Bicicleta_Electrica(VElectricos,Vehiculos):
    pass

mi_bici=Bicicleta_Electrica("Orbea", "Mamalon") #El contructor que hereda es la preferencia de la primera clase que se escribio