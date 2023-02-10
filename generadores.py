def func_pares(limite):
    num = 1
    mi_lista = []

    while num < limite:
        mi_lista.append(num*2)
        num += 1
    return mi_lista

print(func_pares(10))

######################## CON GENERADOR #####################################################


def generar_pares(limite):
    num = 1

    while num < limite:
        yield num*2
        num += 1

devuelve_pares=generar_pares(10)

print(next(devuelve_pares))
# for i in devuelve_pares:
#     print(i)
print("Aqui podria ir mas codigo...")
print(next(devuelve_pares))

print("Aqui podria ir mas codigo...")
print(next(devuelve_pares))
