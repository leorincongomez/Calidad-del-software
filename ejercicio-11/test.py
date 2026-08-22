import unittest
from ejercicio11 import AhorroPersonal

class TestAhorroPersonal(unittest.TestCase):
    def test_saldo_inicial(self):
        ahorro = AhorroPersonal(1000)
        print(f"  [Ahorro Personal] Saldo inicial: ${ahorro.saldoInicial}")
        self.assertEqual(ahorro.saldoInicial, 1000)

    def test_agregar_interes(self):
        ahorro = AhorroPersonal(1000)
        nuevo_saldo = ahorro.agregarInteres(10)
        print(f"  [Agregar Interés 10%] Nuevo saldo: ${nuevo_saldo} (Esperado: $1100)")
        self.assertEqual(nuevo_saldo, 1100)

    def test_prevision_anual(self):
        ahorro = AhorroPersonal(1000)
        prevision = ahorro.previsionAnual(10, 3)
        print(f"  [Previsión a 3 años 10%] Resultado: ${prevision:.2f} (Esperado: $1331.0)")
        self.assertAlmostEqual(prevision, 1331.0, places=2)

if __name__ == '__main__':
    unittest.main()