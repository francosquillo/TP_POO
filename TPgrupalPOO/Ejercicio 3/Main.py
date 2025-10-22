
from Plato import Plato
from Ingrediente import Ingrediente


class MenuRestaurant:
    def __init__(self):
        self.platos_menu = []

    def cargar_platos(self):
        while True:
            print("\n--- Carga de Plato ---")
            nombre = input("Nombre del plato/bebida: ")
            precio = float(input("Precio:$ "))
            tipo = input("¿Es una bebida? (s/n): ").lower()
            es_bebida = (tipo == "s")

            plato = Plato(nombre, precio, es_bebida)

            if not es_bebida:
                while True:
                    print("\n--- Agregar ingrediente ---")
                    nom_ing = input("Nombre del ingrediente: ")
                    cant_ing = float(input("Cantidad: "))
                    unidad = input("Unidad de medida: ")
                    ingrediente = Ingrediente(nom_ing, cant_ing, unidad)
                    plato.agregar_ingrediente(ingrediente)

                    otro = input("¿Desea agregar otro ingrediente? (s/n): ").lower()
                    if otro != "s":
                        break
            else:
                print("→ Plato identificado como bebida. No se solicitan ingredientes.")

            self.platos_menu.append(plato)

            continuar = input("\n¿Desea cargar otro plato? (s/n): ").lower()
            if continuar != "s":
                break

    def mostrar_menu(self):
        print("\n----------- MENÚ ----------------")
        for plato in self.platos_menu:
            print(plato)

    @staticmethod
    def main():
        menu = MenuRestaurant()
        menu.cargar_platos()
        menu.mostrar_menu()


if __name__ == "__main__":
    MenuRestaurant.main()
