# (*agrumento) le estamos diciendo a python que resivira
# un num indeterminados de elementos y los generara en duplas

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        # for sub_elementos in elemento:  # para interar las ciudades por letras
        yield from elemento


ciudades_devueltas = devuelve_ciudades(
    "Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
