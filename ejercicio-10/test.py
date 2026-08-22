import unittest
from calculadorTriangulo import CalculadoraTriangulo

class TestCalculadoraTriangulo(unittest.TestCase):
    def test_calcular_area(self):
        triangulo = CalculadoraTriangulo(6, 4)
        area = triangulo.calcularArea()
        print(f"  [Triángulo base=6, altura=4] Área: {area} (Esperado: 12)")
        self.assertEqual(area, 12)

    def test_area_decimal(self):
        triangulo = CalculadoraTriangulo(5.5, 3.0)
        area = triangulo.calcularArea()
        print(f"  [Triángulo base=5.5, altura=3.0] Área: {area} (Esperado: 8.25)")
        self.assertEqual(area, 8.25)

if __name__ == '__main__':
    unittest.main()
