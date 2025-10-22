from Habitacion import habitacion

class Vivienda:
    def __init__(self, calle, numero, manzana, nro_casa, superficie_terreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nro_casa = nro_casa
        self.superficie_terreno = superficie_terreno
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        total_cubierto = sum(h.metros_cuadrados for h in self.habitaciones)
        if total_cubierto > self.superficie_terreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")
        return total_cubierto
