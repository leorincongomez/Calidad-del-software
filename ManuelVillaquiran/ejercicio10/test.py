import unittest
from calculadoraTriangulo import CalculadoraTriangulo

class TestCalculadoraTriangulo(unittest.TestCase):
    def test_calcular_area(self):
        triangulo = CalculadoraTriangulo(base=6, altura=4)
        area = triangulo.calcularArea()
        print(f"  [ManuelVillaquiran - Triángulo base=6, altura=4] Área: {area} (Esperado: 12)")
        self.assertEqual(area, 12)

if __name__ == '__main__':
    unittest.main()