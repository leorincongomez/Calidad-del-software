class CalculadoraPropina:

    def __init__(self, total, porcentaje):
        self.total = total
        self.porcentaje = porcentaje

    def calcularPropina(self):
        return self.total * self.porcentaje / 100

    def calcularTotal(self):
        return self.total + self.calcularPropina()