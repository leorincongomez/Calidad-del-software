import unittest

from calcular_factura_v2 import CalculadoraFactura


class TestCalculadoraFactura(unittest.TestCase): 
    def test_calcular_subtotal(self):
        factura = CalculadoraFactura(20000, 3, 10) 

        self.assertEqual(factura.calcularSubtotal(), 60000)

    def test_calcular_descuento(self):
        factura = CalculadoraFactura(20000, 3, 10)

        self.assertEqual(factura.calcularDescuento(), 6000)

    def test_calcular_total(self):
        factura = CalculadoraFactura(20000, 3, 10)

        self.assertEqual(factura.calcularTotal(), 54000)

    def test_calcular_total_sin_descuento(self):
        factura = CalculadoraFactura(15000, 2, 0)

        self.assertEqual(factura.calcularTotal(), 30000)

    def test_calcular_total_con_descuento_completo(self):
        factura = CalculadoraFactura(15000, 2, 100)

        self.assertEqual(factura.calcularTotal(), 0)


if __name__ == "__main__":
    unittest.main()
