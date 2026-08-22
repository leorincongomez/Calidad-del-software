import unittest
from calculadora_propina import CalculadoraPropina

class TestCalculadoraPropina(unittest.TestCase):
    def setUp(self):
        self.total, self.porcentaje = 50000, 10
        self.calc = CalculadoraPropina(self.total, self.porcentaje)

    def test_calcular_propina(self):
        propina = self.calc.calcularPropina()
        print(f"  [Propina Total=${self.total}, %={self.porcentaje}] Propina: ${propina} (Esperado: $5000)")
        self.assertEqual(propina, 5000)

    def test_calcular_total(self):
        total_con_propina = self.calc.calcularTotal()
        print(f"  [Total con Propina ${self.total} + ${self.calc.calcularPropina()}] Total: ${total_con_propina} (Esperado: $55000)")
        self.assertEqual(total_con_propina, 55000)

if __name__ == '__main__':
    unittest.main()