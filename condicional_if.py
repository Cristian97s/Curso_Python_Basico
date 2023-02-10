print("Programa de evaluacion de notas de alumnos")

nota_alumno = input("Introduce la nota del alumno: ")
# nota_alumno = input()

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion

# print(evaluacion(4)) #agregando la nota fija
print(evaluacion(int(nota_alumno)))