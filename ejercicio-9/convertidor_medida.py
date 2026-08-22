class ConvertidorMedidas:
    def __init__(self, metros):
        self.metros = metros

    def aCentimetros(self):
        return self.metros * 100

    def aKilometros(self):
        return self.metros / 1000


# Ejemplo de uso
convertidor = ConvertidorMedidas(5)

print("Metros:", convertidor.metros)
print("Centímetros:", convertidor.aCentimetros())
print("Kilómetros:", convertidor.aKilometros())