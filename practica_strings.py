nombre_usuario = input("Introduce- tu nombre de usuario: ")

# print("El nombre de usuario es:", nombre_usuario)
# print("El nombre de usuario es:", nombre_usuario.upper()) #pasarlo a Mayusculas
# print("El nombre de usuario es:", nombre_usuario.lower()) #pasarlo a Minusculas
# la primera letra en Mayusculas
print("El nombre de usuario es:", nombre_usuario.capitalize())

edad = input("Introduce la edad: ")
# print(edad.isdigit()) #valida si lo que un digito

while (edad.isdigit() == False):
    print("Por favor, introduce un valor numerico")
    edad = input("Introduce la edad: ")

if (int(edad) < 18):
    print("no se puede pasar")
else:
    print("puede pasar")
