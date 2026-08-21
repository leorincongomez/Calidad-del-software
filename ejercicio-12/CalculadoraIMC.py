class CalculadoraIMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def obtenerIndice(self):
        return self.peso / (self.altura ** 2)



# Recibe datos del usuario
peso = float(input("Ingrese el peso (kg): "))
altura = float(input("Ingrese la altura (m): "))

calculadora = CalculadoraIMC(peso, altura)

# Obtener el IMC
imc = calculadora.obtenerIndice()

print("El IMC es:", imc)