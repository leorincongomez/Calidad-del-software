class CalculadoraDescuentos:
    def __init__(self, precio, porcentaje):
        self.precio = precio
        self.porcentaje = porcentaje

    def montoDescuento(self):
        return self.precio * self.porcentaje / 100

    def precioFinal(self):
        return self.precio - self.montoDescuento()


# Ejemplo de uso
precio = float(input("Ingrese el precio: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))

compra = CalculadoraDescuentos(precio, porcentaje)
print("Monto de descuento:", compra.montoDescuento())
print("Precio final:", compra.precioFinal())
