# for letra in "Python":

#     # a cada vuelta evalua la condicion y cuando se
#     # cumpla lo que hara sera ignorar el resto del bucle y pasar a la siguite interacion
#     if letra == "h":
#         continue

#     print("viendo la letra: " + letra)

############################### CONTINUE #######################################################

# nombre = "estoy mamadisimo, de veras"
# print(len(nombre))

# contador = 0

# for i in nombre:
#     if i == " ":
#         continue

#     contador += 1  # es equivalente ///contador = contador +1///

# print(contador)

################################### ELSE ######################################################

email = input("introduce tu email, por favor: ")

for i in email:
    if i == "@":
        arroba=True
        break

else:
    arroba=False

print(arroba)

################################### PASS ######################################################

# # se unsa para salir de un bucle
# while True:
#     pass

# # cuando creamos una clase que en el futuro completaremos
# class MiClase:
#     pass #para implementar mas tarde
