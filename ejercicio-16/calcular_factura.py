class CalculadoraFactura:

    def __init__(self, precio, cantidad, descuento):
        self.precio = precio
        self.cantidad = cantidad
        self.descuento = descuento

    def calcularSubtotal(self):
        return self.precio * self.cantidad

    def calcularDescuento(self):
        subtotal = self.calcularSubtotal()
        return subtotal * self.descuento / 100

    def calcularTotal(self):
        subtotal = self.calcularSubtotal()
        descuento = self.calcularDescuento()
        return subtotal - descuento


if __name__ == "__main__":
    # Crear objeto
    factura = CalculadoraFactura(20000, 3, 10)

    print("Subtotal:", factura.calcularSubtotal())
    print("Descuento:", factura.calcularDescuento())
    print("Total:", factura.calcularTotal())