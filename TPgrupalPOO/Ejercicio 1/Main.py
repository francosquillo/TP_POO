class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

class Matriz:
    def __init__(self):
        self.matriz_celda = []

    def agregar_celda(self, celda_agregar):
        self.matriz_celda.append(celda_agregar)

    def mostrar_matriz(self):
        for i in self.matriz_celda:
            print(f"Fila:{i.fila},Columna:{i.columna},Valor:{i.valor}")
    
    def buscar_duplicados(self,fila,columna):
        for i in self.matriz_celda:
            if fila == i.fila and columna==i.columna:
                print("valor ya existente")
                return False
        return True
    
    def buscar_valor(self,fila,columna):
        for i in self.matriz_celda:
            if fila==i.fila and columna==i.columna:
                return f"El valor es {i.valor}"
                
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

matriz1 = Matriz()

while True:
    fila_ingreso = int(input("Ingrese la fila a la que desea agregar un valor: "))
    columna_ingreso = int(input("Ingrese la columna a la que desea agregar un valor: "))
    valor_ingreso = input("Ingrese el valor que desea añadir: ")
    duplicado=matriz1.buscar_duplicados(fila_ingreso,columna_ingreso)
    if duplicado==True:
        nueva_celda = Celda(fila_ingreso, columna_ingreso, valor_ingreso)
        matriz1.agregar_celda(nueva_celda)
        print("Valor agregado con exito")

    salir=input("Si desea salir escriba fin: ")
    if salir=="fin":
        break
    
matriz1.mostrar_matriz()

fila_busca=int(input("Ingrese la fila del valor que desea buscar: "))
columna_busca=int(input("Ingrese la columna del valor que desea buscar: "))
print(matriz1.buscar_valor(fila_busca,columna_busca))