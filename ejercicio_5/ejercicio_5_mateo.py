class CalculadoraIVA:
    def __init__(self, precioBase):
        self.precioBase = precioBase

    def obtenerIVA(self):
        return self.precioBase * 0.21

    def precioTotal(self):
        return self.precioBase + self.obtenerIVA()


precio = float(input("Ingrese el precio base: "))
calc = CalculadoraIVA(precio)
print("IVA:", calc.obtenerIVA())
print("Total:", calc.precioTotal())