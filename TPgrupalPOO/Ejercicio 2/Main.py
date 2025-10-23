from alumnos import alumnos
from notas import nota

class carganotas:
    def __init__(self):
        self.lista_alumnos = []

    def main(self):
        while True:
            print("CARGA DE DATOS DEL ALUMNO")
            nombre_carga = input("Ingrese el nombre completo del alumno: ")
            legajo_ingresar = int(input("Ingrese el legajo del alumno: "))
            alumno = alumnos(nombre_carga, legajo_ingresar)

            while True:
                catedra_agregar = input("Ingrese el nombre de la cátedra: ")
                nota_agregar = int(input("Ingrese la nota: "))
                nota_agregar = nota(catedra_agregar, nota_agregar)
                alumno.cargar_notas(nota_agregar)

                salir = (input("Ingrese 1 si desea salir de la carga de notas: "))
                if salir == "1":
                    break

            self.lista_alumnos.append(alumno)

            salir = (input("Ingrese 1 si desea salir de la carga de alumnos: "))
            if salir == "1":
                break

        print("\n--- LISTA DE ALUMNOS ---")
        for i in self.lista_alumnos:
            i.imprimir_datos()
            i.calculo_promedio()

if __name__ == "__main__":
    programa = carganotas()
    programa.main()

