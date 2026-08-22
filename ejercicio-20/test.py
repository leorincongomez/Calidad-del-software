import unittest
from calculadora_interes import CalculadoraInteres

class TestCalculadoraInteres(unittest.TestCase):
    def setUp(self):
        self.capital, self.tasa, self.tiempo = 1000, 5, 2
        self.calc = CalculadoraInteres(self.capital, self.tasa, self.tiempo)

    def test_calcular_interes(self):
        interes = self.calc.calcularInteres()
        print(f"  [Interés Simple Cap=${self.capital}, Tasa={self.tasa}%, Tiempo={self.tiempo}años] Interés: ${interes} (Esperado: $100)")
        self.assertEqual(interes, 100.0)

    def test_calcular_monto(self):
        monto = self.calc.calcularMonto()
        print(f"  [Monto Final Cap=${self.capital} + Interés=$100] Monto total: ${monto} (Esperado: $1100)")
        self.assertEqual(monto, 1100.0)

if __name__ == '__main__':
    unittest.main()
