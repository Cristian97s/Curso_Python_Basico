midiccionario = {"Alemania": "Berlín", "Francia": "París",
                 "Reino Unido": "Londres", "Espana": "Madrid"}

# Agregar un nuevo elemento al diccionario
midiccionario["Italia"] = "Lisboa"

# Imprimimos por la clave valor
print(midiccionario["Francia"])

# Imprimir todo el diccionario
print(midiccionario)

# Modificar un valor que le adcinamos a la clave
midiccionario["Italia"] = "Roma"
print(midiccionario)


# Eliminar un elemento
del midiccionario["Reino Unido"]
print(midiccionario)

# Diccionario con valores alternos
midiccionario1 = {"Alemania": "Berlín", 23: "Jordan", "Mosqueteros": 3}
print(midiccionario1)

# Utilizar una tupla para accinar claves a los valores
mitupla = ["Espana", "Francia", "Reino Unido", "Alemania"]
midiccionario2 = {mitupla[0]: "Madrid", mitupla[1]
    : "París", mitupla[2]: "Londres", mitupla[3]: "Berlín"}
print(midiccionario2)
# Acceder a un elemento concreto
print(midiccionario2["Francia"])

# Diccionario almacenando una tupla
midiccionario3 = {23: "Jordan", "Nombre": "Michael",
                  "Equipo": "Chicago", "anillos": [1991, 1992, 1993, 1996, 1997, 1998]}
print(midiccionario3["anillos"])

# Guardar un diccionario dentro de otro diccionario
midiccionario4 = {23: "Jordan", "Nombre": "Michael",
                  "Equipo": "Chicago", "anillos": {"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(midiccionario4["anillos"])

# Metodos con Diccionarios
print(midiccionario4.keys()) # me manda todas las claves de este diccionario
print(midiccionario4.values()) # si necesito que me imprima los valores
print(len(midiccionario4)) # conocer la longitud del diccionario
print(midiccionario4)