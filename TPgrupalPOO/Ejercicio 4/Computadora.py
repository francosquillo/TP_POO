from ComponenteCPU import ComponenteCPU

class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def costo_total(self):
        return sum(c.subtotal() for c in self.componentes)

    def precio_venta(self):
        costo = self.costo_total()
        if costo < 50000:
            return costo * 1.40
        else:
            return costo * 1.30

    def mostrar_informacion(self):
        print("\n----------- Computadora ----------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("Componentes:")
        print("Componente           | Marca           | Cantidad | Precio X    | Unidad SubTotal")
        print("-" * 80)
        for c in self.componentes:
            print(c)
        print("-" * 80)
        print(f"Costo Total  : {self.costo_total():.2f}")
        print(f"El precio sugerido de venta es {self.precio_venta():.2f}")
