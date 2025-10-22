from vivienda import Vivienda

class Barrio:
    def __init__(self, nombre, empresa_constructora):
        self.nombre = nombre
        self.empresa_constructora = empresa_constructora
        self.viviendas = []

    def agregar_vivienda(self, vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self):
        return sum(v.superficie_terreno for v in self.viviendas)

    def getSuperficieTotalTerrenoXManzana(self, manzana):
        return sum(v.superficie_terreno for v in self.viviendas if v.manzana == manzana)

    def getSuperficieTotalCubierta(self):
        total = 0
        for v in self.viviendas:
            total += v.getMetrosCuadradosCubiertos()
        return total
