import unittest
from calculadora_area_cuadrado import CalculadoraAreaCuadrado

class TestCalculadoraAreaCuadrado(unittest.TestCase):
    def setUp(self):
        self.lado = 5
        self.cuadrado = CalculadoraAreaCuadrado(self.lado)

    def test_calcular_area(self):
        area = self.cuadrado.calcularArea()
        print(f"  [Cuadrado lado={self.lado}] Área calculada: {area} (Esperado: 25)")
        self.assertEqual(area, 25)

    def test_calcular_perimetro(self):
        perimetro = self.cuadrado.calcularPerimetro()
        print(f"  [Cuadrado lado={self.lado}] Perímetro calculado: {perimetro} (Esperado: 20)")
        self.assertEqual(perimetro, 20)

if __name__ == '__main__':
    unittest.main()
