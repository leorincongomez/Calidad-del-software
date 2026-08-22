class CalculadoraBasica:

    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2


if __name__ == "__main__":
    calculadora = CalculadoraBasica()
    print("Suma:", calculadora.sumar(10, 5))
    print("Resta:", calculadora.restar(10, 5))