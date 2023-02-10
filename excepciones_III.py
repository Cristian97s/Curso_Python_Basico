# def evalua_edad(edad):

#     if edad<0:
#         #personalizamos la excepcion
#         raise TypeError("No se permiten edades negativas")
#     elif edad <20:
#         return "eres muy joven"
#     elif edad<40:
#         return "eres joven"
#     elif edad<65:
#         return "eres maduro"
#     elif edad<100:
#         return "cuidate..."

# print(evalua_edad(-18))

####################################################################################################

import math

def calcula_raiz(num1):

    if num1<0:
        raise ValueError ("El número no puede ser negativo")
    
    else:
        return math.sqrt(num1)

try:
    op1=(int(input("Introduce un número: ")))
    print(calcula_raiz(op1))

except ValueError as ErrorDeNumNegativo:
    print(ErrorDeNumNegativo)

print("Programa terminado")