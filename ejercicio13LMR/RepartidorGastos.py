class RepartidorGastos:
    def __init__(self, totalFactura, numeroPersonas):
        self.totalFactura = totalFactura
        self.numeroPersonas = numeroPersonas

    def divisionEquitativa(self):
        return self.totalFactura / self.numeroPersonas