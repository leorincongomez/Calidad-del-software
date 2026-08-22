import unittest
from calcular_factura_v2 import CalculadoraFactura

class TestCalculadoraFactura(unittest.TestCase): 
    def test_calcular_subtotal(self):
        factura = CalculadoraFactura(20000, 3, 10) 
        subtotal = factura.calcularSubtotal()
        print(f"  [Factura $20000 x 3] Subtotal: ${subtotal} (Esperado: $60000)")
        self.assertEqual(subtotal, 60000)

    def test_calcular_descuento(self):
        factura = CalculadoraFactura(20000, 3, 10)
        desc = factura.calcularDescuento()
        print(f"  [Factura Subtotal=$60000, desc=10%] Descuento: ${desc} (Esperado: $6000)")
        self.assertEqual(desc, 6000)

    def test_calcular_total(self):
        factura = CalculadoraFactura(20000, 3, 10)
        total = factura.calcularTotal()
        print(f"  [Factura $20000 x 3 desc 10%] Total: ${total} (Esperado: $54000)")
        self.assertEqual(total, 54000)

    def test_calcular_total_sin_descuento(self):
        factura = CalculadoraFactura(15000, 2, 0)
        total = factura.calcularTotal()
        print(f"  [Factura $15000 x 2 desc 0%] Total: ${total} (Esperado: $30000)")
        self.assertEqual(total, 30000)

    def test_calcular_total_con_descuento_completo(self):
        factura = CalculadoraFactura(15000, 2, 100)
        total = factura.calcularTotal()
        print(f"  [Factura $15000 x 2 desc 100%] Total: ${total} (Esperado: $0)")
        self.assertEqual(total, 0)

if __name__ == "__main__":
    unittest.main()
