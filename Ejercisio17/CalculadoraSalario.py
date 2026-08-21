class CalculadoraSalario:
    def __init__(self, salarioBase, horasExtra):
        self.salarioBase = salarioBase
        self.horasExtra = horasExtra

    def calcularPagoExtra(self):
        return self.horasExtra * 10

    def calcularSalarioTotal(self):
        return self.salarioBase + self.calcularPagoExtra()


salario = CalculadoraSalario(1000, 5)

print("Pago por horas extra:", salario.calcularPagoExtra())
print("Salario total:", salario.calcularSalarioTotal())
