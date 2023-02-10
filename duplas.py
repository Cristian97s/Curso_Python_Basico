mitupla = ("Cris", 21, 9, 1997)
# Aceder a un elemento
print(mitupla[1])

# Convertir una tupla a lista
milista = list(mitupla)
print(milista)

# Convertir una lista a tupla
milista1 = ["Cris", 21, 9, 1997, 21]
mitupla1 = tuple(milista1)
print(mitupla1)

# Comprobar si ahi elementos
print("Cris" in mitupla1)

# Cuantos elementos se encuentra en la tupla
print(mitupla1.count(21))

# Averiguar la longitud de una tupla (esto no te da los indeces si no cuantos elementos ahi)
print(len(mitupla1))

# Tupla unitaria
mitupla2 = ("Cris",)
print(len(mitupla2))

# Empaquetado de tupla
# Puedo escribir una tupla precindiendo de los parantesis
mitupla3 = "Cris", 21, 9, 1997
print(mitupla3)

# Desempaquetado de tupla
mitupla4 = ("Cris", 21, 9, 1997)
nombre, dia, mes, agno = mitupla4
print(nombre)
print(dia)
print(agno)
print(mes)

# Obtener el indece del elemento en la tupla
print(mitupla4.index("Cris"))