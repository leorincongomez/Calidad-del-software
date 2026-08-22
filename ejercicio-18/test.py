import unittest
from calculadora_combustible import CalculadoraCombustible

class TestCalculadoraCombustible(unittest.TestCase):
    def setUp(self):
        self.distancia, self.consumo = 200, 0.08
        self.calc = CalculadoraCombustible(self.distancia, self.consumo)

    def test_calcular_combustible(self):
        litros = self.calc.calcularCombustibleNecesario()
        print(f"  [Combustible dist={self.distancia}km, consumo={self.consumo}L/km] Litros: {litros} L (Esperado: 16 L)")
        self.assertEqual(litros, 16.0)

    def test_calcular_costo_viaje(self):
        precio = 50
        costo = self.calc.calcularCostoViaje(precio)
        print(f"  [Costo Viaje 16L x ${precio}/L] Costo total: ${costo} (Esperado: $800)")
        self.assertEqual(costo, 800.0)

if __name__ == '__main__':
    unittest.main()
