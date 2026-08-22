import unittest
from RepartidorGastos import RepartidorGastos

class TestRepartidorGastos(unittest.TestCase):
    def test_division_equitativa(self):
        total, personas = 150000, 5
        gasto = RepartidorGastos(total, personas)
        resultado = gasto.divisionEquitativa()
        print(f"  [Gastos Total=${total}, Personas={personas}] Pago por persona: ${resultado:.2f} (Esperado: $30000)")
        self.assertEqual(resultado, 30000)

if __name__ == '__main__':
    unittest.main()