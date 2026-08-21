class CalculadoraSalario:
    def __init__(self, salarioBase, horasExtra):
        self.salarioBase = salarioBase
        self.horasExtra = horasExtra

    def calcularPagoExtra(self):
        return self.horasExtra * 10

    def calcularSalarioTotal(self):
        return self.salarioBase + self.calcularPagoExtra()


# Pedir datos al usuario
salarioBase = float(input("Ingrese el salario base: "))
horasExtra = int(input("Ingrese las horas extra: "))

# Crear el objeto
salario = CalculadoraSalario(salarioBase, horasExtra)

# Mostrar resultados
print("Pago por horas extra:", salario.calcularPagoExtra())
print("Salario total:", salario.calcularSalarioTotal())
