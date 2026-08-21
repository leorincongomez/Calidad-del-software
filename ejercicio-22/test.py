from calculadora_propina import CalculadoraPropina

calculadora = CalculadoraPropina(50000, 10)

print("Total de la cuenta:", calculadora.total)
print("Propina:", calculadora.calcularPropina())
print("Total con propina:", calculadora.calcularTotal())