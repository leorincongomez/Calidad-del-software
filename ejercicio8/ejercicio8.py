entradaUsuario = input("si quiere sacar el area ingresa A y si quieres sacar la circunferencia ingresa C: ")

def area(radio):
    area = 3.1416*radio**2
    print(f"el area de tu circulo es: {area}")

def circunferencia(radio):
    circunferencia = 2*3.1416*radio
    print(f"la circunferencia de tu circulo es {circunferencia}")


if entradaUsuario.upper() == "A":
    radio = float(input("ingresa el radio de tu circulo para realizar la operacion: "))
    area(radio)
elif entradaUsuario.upper() == "C":
    radio = float(input("ingresa el radio de tu circulo para realizar la operacion: "))
    circunferencia(radio)

