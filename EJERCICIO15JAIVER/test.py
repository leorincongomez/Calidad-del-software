from jaiver15 import AnalisisNumerico

def test_analisis_numerico():
    # Caso 1: número par
    an1 = AnalisisNumerico(10)
    assert an1.esPar() == True, "10 debería ser par"
    assert an1.obtenerDoble() == 20, "El doble de 10 debería ser 20"

    # Caso 2: número impar
    an2 = AnalisisNumerico(7)
    assert an2.esPar() == False, "7 debería ser impar"
    assert an2.obtenerDoble() == 14, "El doble de 7 debería ser 14"

    # Caso 3: número negativo
    an3 = AnalisisNumerico(-4)
    assert an3.esPar() == True, "-4 debería ser par"
    assert an3.obtenerDoble() == -8, "El doble de -4 debería ser -8"

    # Caso 4: cero
    an4 = AnalisisNumerico(0)
    assert an4.esPar() == True, "0 debería ser par"
    assert an4.obtenerDoble() == 0, "El doble de 0 debería ser 0"

    print("Todas las pruebas de AnalisisNumerico pasaron correctamente ✅")


if __name__ == "__main__":
    test_analisis_numerico()