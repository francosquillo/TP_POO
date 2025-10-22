class Ingrediente:
    def __init__(self, nombre: str, cantidad: float, unidad_medida: str):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida

    def __str__(self):
        return f"{self.nombre:<10} | {self.cantidad:<10} | {self.unidad_medida}"