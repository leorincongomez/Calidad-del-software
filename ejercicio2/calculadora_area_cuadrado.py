class CalculadoraAreaCuadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado

    def calcularPerimetro(self):
        return 4 * self.lado


lado = float(input("Ingrese el lado del cuadrado: "))

cuadrado = CalculadoraAreaCuadrado(lado)

print("Área del cuadrado:", cuadrado.calcularArea())
print("Perímetro del cuadrado:", cuadrado.calcularPerimetro())