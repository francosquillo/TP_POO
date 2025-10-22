

from Ingrediente import Ingrediente

class Plato:
    def __init__(self, nombre_completo: str, precio: float, es_bebida: bool):
        self.nombre_completo = nombre_completo
        self.precio = precio
        self.es_bebida = es_bebida
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)

    def __str__(self):
        salida = f"{self.nombre_completo}\nPrecio: $ {self.precio:.2f}\n"
        if not self.es_bebida:
            salida += "Ingredientes:\n"
            salida += f"{'Nombre':<10} | {'Cantidad':<10} | Unidad de Medida\n"
            for ing in self.ingredientes:
                salida += f"{ing}\n"
        salida += "-" * 60
        return salida