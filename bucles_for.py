for i in [1, 2, 3]:
    print("hola")

for estaciones in ["primavera", "verano", "otoño", "invierno"]:
    print(estaciones)

for i in ["Pildoras", "Informatica", 3]:
    print("hola", end=" ")

########################################################################################

# Evaluar si un correo es correcta si tiene @
contador = False
punto = 0
mi_email = input("Introduce tu direccion de Email: ")
# #mi_email = "cristian.aleman1997@gmail.com"
# #print(mi_email)

for i in mi_email:
    if i == "@" or i == ".":
        # si no ahi [@ ó .] sera \\0\\ "en caso contrario 1 y si cumple los dos sera 2"
        contador = contador + 1
        if i == ".":
            punto = punto + 1

if contador == 2 or punto >= 0:
    print("Email es correcto")
else:
    print("Email es incorrecto")

# AUN FALTA MEJORAR EL CODIGO

##########################################################################################

for i in range(5):
    print("hola")
    print(i)
