class CalculadoraBasica:

    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2


# Ejemplo de uso
calculadora = CalculadoraBasica()

print("Suma:", calculadora.sumar(10, 5))
print("Resta:", calculadora.restar(10, 5))