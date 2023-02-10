##### PRIMERA FUNCION #####

def mensaje():
    print("Estoy aprendiendo python")
    print("Estamos aprendiendo eintruciones basicas")
    print("Poco a poco iremos avanzando")

mensaje()

print("Ejecutando código fuera de la función")

#### FUNCION suma sin parametros ####

def suma():
    num1=3
    num2=4
    print(num1+num2) #7

suma()

#### FUNCION suma CON PARAMETROS ####

def suma1(num1, num2):
    print(num1+num2)

suma1(2,3)

### FUNCION suma CON RETURN ####

def suma3(num1, num2):
    resultado=num1+num2
    return resultado

print(suma3(9,1))

almacena_resultado=suma3(5,8)

print(almacena_resultado)