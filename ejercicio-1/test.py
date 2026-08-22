import unittest
from CalculadoraBasica import CalculadoraBasica

class TestCalculadoraBasica(unittest.TestCase):
    def setUp(self):
        self.calc = CalculadoraBasica()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(10, 5), 15)
        self.assertEqual(self.calc.sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 5), 5)
        self.assertEqual(self.calc.restar(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
