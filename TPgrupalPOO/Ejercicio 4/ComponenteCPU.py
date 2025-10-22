class ComponenteCPU:
    def __init__(self, componente, marca, cantidad, precio):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    def subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f"{self.componente:20} | {self.marca:15} | {self.cantidad:7} | {self.precio:12.2f} | {self.subtotal():12.2f}"

