import unittest
from CalculadoraBasica import CalculadoraBasica

class TestCalculadoraBasica(unittest.TestCase):
    def setUp(self):
        self.calc = CalculadoraBasica()

    def test_sumar(self):
        a, b = 10, 5
        res = self.calc.sumar(a, b)
        print(f"  [Suma] {a} + {b} = {res} (Esperado: 15)")
        self.assertEqual(res, 15)

    def test_restar(self):
        a, b = 10, 5
        res = self.calc.restar(a, b)
        print(f"  [Resta] {a} - {b} = {res} (Esperado: 5)")
        self.assertEqual(res, 5)

if __name__ == '__main__':
    unittest.main()
