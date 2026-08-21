class OperacionesPotencia:

    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcularPotencia(self):
        resultado = 1

        for i in range(self.exponente):
            resultado = resultado * self.base

        return resultado

    def calcularCuadrado(self):
        resultado = self.base * self.base
        return resultado


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

operacion = OperacionesPotencia(base, exponente)

print("Potencia:", operacion.calcularPotencia())
print("Cuadrado:", operacion.calcularCuadrado())