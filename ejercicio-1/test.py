from CalculadoraBasica import CalculadoraBasica

calculadora = CalculadoraBasica()

resultado_suma = calculadora.sumar(10, 5)
resultado_resta = calculadora.restar(10, 5)

print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)

assert resultado_suma == 15
assert resultado_resta == 5

print("Todas las pruebas fueron exitosas.")