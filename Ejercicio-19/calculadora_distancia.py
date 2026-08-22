class CalculadoraDistancia:

    def __init__(self, distanciaInicial, distanciaFinal):
        self.distanciaInicial = distanciaInicial
        self.distanciaFinal = distanciaFinal

    def calcularDistancia(self):
        return self.distanciaFinal - self.distanciaInicial