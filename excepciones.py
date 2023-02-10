def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:  # si el error conside con el except ejecutara el error que esta dentro de el
        print("No se puede dividir entre 0")
        return "Operación Errónea"

while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))
        op2 = (int(input("Indroduce el segundo número: ")))

        break
    except ValueError: #aqui atrapo el error y le pido que ingrese valores numericos
        print("Los valores son incorrecto, vuelve a intendarlo")

operacion = input(
    "Introduce la operación a realizar (Suma, Resta, Multiplica, Divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa")
