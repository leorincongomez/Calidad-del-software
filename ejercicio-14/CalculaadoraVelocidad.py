class CalculadoraVelocidad:
    def __init__(self, distancia, tiempo):
        self.distancia = distancia
        self.tiempo = tiempo

    def calcularVelocidadMedia(self):
        return self.distancia / self.tiempo


if __name__ == "__main__":
    distancia = float(input("Ingrese la distancia recorrida en kilometros: "))
    tiempo = float(input("Ingrese el tiempo en horas: "))
    calculadora = CalculadoraVelocidad(distancia, tiempo)
    velocidad = calculadora.calcularVelocidadMedia()
    print("La velocidad media es:", velocidad, "km/h")