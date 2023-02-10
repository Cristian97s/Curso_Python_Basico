miLista = ["María", "Pepe", "Marta", "Antonio"]

# Llamo todos los elementos de la lista
print(miLista[:])

# Si quiero acceder a un elemento
print(miLista[2])

# Si introdusco un indice negativo, empieza a contar el indice desde el final
print(miLista[-3])

# Procion de lista (acceder a un troso de la lista)
print(miLista[0:3])

print(miLista[1:3])

# Prociones abreviadas
print(miLista[:2])

print(miLista[2:])

### Agregar elementos a la lista

miLista.append("Sandra") #append agrega al final de la lista
miLista.insert(2,"Sandra") #insert agrega en la posicion que insertes
miLista.extend(["Sandra","Ana", "Licia"]) # agregar varios elementos a la lista (concatena)
print(miLista.index("Ana")) # obtener el indice del elemento

print("Pepe" in miLista) #pregunto si pepe esta en la lista

print(miLista[:])

# Lista con varios tipos de elementos
miLista2 = ["Maria", 5, True, 78.35]
miLista2.extend(["Sandra", "Ana", "Lucia"])

miLista2.remove("Ana")  # elimina un elemento a elegir

print(miLista2[2])

miLista2.pop()  # elimina el ultimo elemento de la lista

print(miLista2[:])

### OPERACIONES CON LISTAS

# unir listas
miLista3 = ["Manolo", "Pedro"]
listaUnion = miLista2+miLista3

print(listaUnion[:])

# repedir listas
miLista4=["Cris", "Bartolomeo", "Mari"] * 3

print(miLista4[:])