class ConversorTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def aFahrenheit(self):
        return self.celsius * 9/5 + 32
    

    def aKelvin(self):

        return self.celsius + 273.15


# Ejemplo de uso
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
temp = ConversorTemperatura(celsius)
print(f"{temp.celsius}°C es igual a {temp.aFahrenheit()}°F")
print(f"{temp.celsius}°C es igual a {temp.aKelvin()}K")