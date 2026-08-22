import unittest
from CalculadoraIMC import CalculadoraIMC

class TestCalculadoraIMC(unittest.TestCase):
    def test_obtener_indice(self):
        peso, altura = 70, 1.75
        calc = CalculadoraIMC(peso, altura)
        imc = calc.obtenerIndice()
        print(f"  [IMC peso={peso}kg, altura={altura}m] IMC calculado: {imc:.2f} (Esperado: 22.86)")
        self.assertAlmostEqual(imc, 22.857, places=3)

if __name__ == '__main__':
    unittest.main()
