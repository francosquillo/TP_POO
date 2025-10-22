class alumnos:
    def __init__(self,nombre_completo,legajo):
        self.nombre_completo=nombre_completo
        self.legajo=legajo
        self.notas=[]

    def calculo_promedio(self):
        contador=0
        promedio=0
        for i in self.notas:
            promedio+=i.notafinal
            contador+=1
        promedio=promedio//contador
        print(f"El promedio de {self.nombre_completo} es {promedio}")
    
    def cargar_notas(self,notas_cargar):
        self.notas.append(notas_cargar)
    
    def imprimir_datos(self):
        print(self.nombre_completo)
        print(self.legajo)
        for i in self.notas:
            print (f"Catedra:{i.catedra}/Nota:{i.notafinal}")