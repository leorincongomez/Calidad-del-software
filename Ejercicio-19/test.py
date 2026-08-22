import unittest
from calculadora_distancia import CalculadoraDistancia

class TestCalculadoraDistancia(unittest.TestCase):
    def test_calcular_distancia(self):
        inicial, final = 50, 150
        calc = CalculadoraDistancia(inicial, final)
        dist = calc.calcularDistancia()
        print(f"  [Distancia pos_inicial={inicial}, pos_final={final}] Distancia recorrida: {dist} (Esperado: 100)")
        self.assertEqual(dist, 100)

if __name__ == '__main__':
    unittest.main()
