import unittest
from CalculaadoraVelocidad import CalculadoraVelocidad

class TestCalculadoraVelocidad(unittest.TestCase):
    def test_calcular_velocidad_media(self):
        distancia, tiempo = 120, 2
        calc = CalculadoraVelocidad(distancia, tiempo)
        vel = calc.calcularVelocidadMedia()
        print(f"  [Velocidad dist={distancia}km, tiempo={tiempo}h] Velocidad media: {vel} km/h (Esperado: 60.0 km/h)")
        self.assertEqual(vel, 60.0)

if __name__ == '__main__':
    unittest.main()
