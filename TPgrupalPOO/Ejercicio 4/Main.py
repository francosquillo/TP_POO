
from Computadora import Computadora
from ComponenteCPU import ComponenteCPU

def main():
    while True:
        marca_pc = input("Ingrese la marca de la computadora: ")
        modelo_pc = input("Ingrese el modelo de la computadora: ")

        computadora = Computadora(marca_pc, modelo_pc)

        n = int(input("Ingrese la cantidad de componentes que desea cargar: "))
        for i in range(n):
            print(f"\nComponente {i+1}:")
            componente = input("Nombre del componente: ")
            marca = input("Marca del componente: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio por unidad: "))
            comp = ComponenteCPU(componente, marca, cantidad, precio)
            computadora.agregar_componente(comp)

        computadora.mostrar_informacion()

        continuar = input("\n¿Desea cotizar una nueva computadora? (SI/NO): ").strip().upper()
        if continuar != "SI":
            print("\nPrograma finalizado.")
            break

if __name__ == "__main__":
    main()
