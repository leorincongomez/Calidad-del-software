class CalculadoraInteres:

    def __init__(self, capital, tasa, tiempo):
        self.capital = capital
        self.tasa = tasa
        self.tiempo = tiempo

    def calcularInteres(self):
        return self.capital * (self.tasa / 100) * self.tiempo

    def calcularMonto(self):
        return self.capital + self.calcularInteres()


if __name__ == "__main__":
    # ingresar los datos
    capital = float(input("Ingrese el capital: "))
    tasa = float(input("Ingrese la tasa de interés (%): "))
    tiempo = float(input("Ingrese el tiempo en años: "))
    calculadora = CalculadoraInteres(capital, tasa, tiempo)
    print("\n--- RESULTADOS ---")
    print("Interés generado:", calculadora.calcularInteres())
    print("Monto final:", calculadora.calcularMonto())