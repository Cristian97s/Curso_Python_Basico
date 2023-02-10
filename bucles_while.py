# i = 1
# while i <= 10:
#     print("ejecucion " + str(i))
#     i = i+1

# print("termino la ejecucion")

#########################################################################################

# edad = int(input("Introduce tu edad por favor: "))

# while edad < 5 or edad > 100:
#     print("Has introducido una edad incorrecta. vuelva a intentarlo")
#     edad = int(input("introduce tu edad por favor: "))

# print("Gracias por colaborar. puedes pasar")
# print("Edad del aspirante " + str(edad))

##########################################################################################
import math

print("programa de calculo de raiz cuadrada")

numero = int(input("Introduce un número por favor: "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break

    numero = int(input("Introduce un número por favor: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("la raíz cuadrada de " + str(numero) + " es " + str(solucion))
