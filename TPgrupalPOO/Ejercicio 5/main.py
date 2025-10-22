from barrio import Barrio
from vivienda import Vivienda
from Habitacion import habitacion

# Crear el barrio
barrio_judicial = Barrio("Barrio Judicial", "Constructora Mendoza SRL")

# Crear viviendas en el barrio
v1 = Vivienda("Ascasubi", 3033, "A", 1, 200)
v2 = Vivienda("Ascasubi", 3050, "A", 2, 180)

# Agregar habitaciones a cada vivienda
v1.agregar_habitacion(habitacion("Dormitorio", 50))
v1.agregar_habitacion(habitacion("Cocina", 25))
v1.agregar_habitacion(habitacion("Baño", 10))

v2.agregar_habitacion(habitacion("Dormitorio", 40))
v2.agregar_habitacion(habitacion("Living", 35))
v2.agregar_habitacion(habitacion("Cocina", 20))

# Asociar viviendas al barrio
barrio_judicial.agregar_vivienda(v1)
barrio_judicial.agregar_vivienda(v2)

# Mostrar resultados
print(f" Barrio: {barrio_judicial.nombre}")
print(f"Constructora: {barrio_judicial.empresa_constructora}")
print(f"Superficie total del barrio: {barrio_judicial.getSuperficieTotalTerreno()} m²")
print(f"Superficie total cubierta del barrio: {barrio_judicial.getSuperficieTotalCubierta()} m²")
print(f"Superficie total de la manzana A: {barrio_judicial.getSuperficieTotalTerrenoXManzana('A')} m²")

# Mostrar detalle por vivienda
for v in barrio_judicial.viviendas:
    print(f"\n Vivienda en {v.calle} {v.numero}, Manzana {v.manzana}")
    print(f" - Superficie del terreno: {v.superficie_terreno} m²")
    print(f" - Superficie cubierta: {v.getMetrosCuadradosCubiertos()} m²")
