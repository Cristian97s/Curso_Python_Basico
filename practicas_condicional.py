edad = -7

if 0 < edad < 100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")

#######################################################################################

salario_presidente = int(input("Introduce salario presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce salario director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area = int(input("Introduce salario jefe_area: "))
print("Salario jefe_area: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce salario administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo anda mal")

#########################################################################################

print("Programa de becas")
distancia_escuela = int(input("Introduce la distancia a la escuela en KM: "))
print(distancia_escuela)

numero_hermnanos = int(input("Ingrese el n° de hemanos en el centro: "))
print(numero_hermnanos)

salario_familiar = int(input("Introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermnanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

##########################################################################################

print("Asignaturasoptativas")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion = input("Escribe la asignatura escogida: ")

# lower(), upper(). la 1° todo en minusculas y la 2° todo en mayusculas
asignatura = opcion.lower()

if asignatura in ("informatica grafica", "prueba de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura escogida no esta contemplada")
