print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad, por favor: "))

# elif lo que se consige es que
# el else se acompañe con toda la condicion
if edad_usuario < 18:
    print("No puedes pasar")
elif edad_usuario > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

print("El programa ha finalizado")

################################################################

print("Verificacion de notas")

nota_alumno = int(input("Introduce tu nota, por favor: "))

if nota_alumno < 5:
    print("Insuficiente")
elif nota_alumno < 6:
    print("Suficiente")
elif nota_alumno < 7:
    print("Bien")
elif nota_alumno < 9:
    print("Notable")
elif nota_alumno <= 100:
    print("Mamalon")
else:  # este else solo esta en el if que lo acompaña
    print("La nota tiene que ser menor de 100")
