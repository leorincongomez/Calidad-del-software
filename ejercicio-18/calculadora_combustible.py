class CalculadoraCombustible:
    def __init__(self, distancia, consumo_por_km):
        self.distancia = distancia
        self.consumo_por_km = consumo_por_km
        
    def calcularCombustibleNecesario(self):
        return self.distancia * self.consumo_por_km
        
    def calcularCostoViaje(self, precio_litro):
        litros_necesarios = self.calcularCombustibleNecesario()
        return litros_necesarios * precio_litro