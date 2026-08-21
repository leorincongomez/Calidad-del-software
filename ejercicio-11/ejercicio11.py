class AhorroPersonal:
    def __init__(self, saldoInicial):
        self.saldoInicial = saldoInicial

    def agregarInteres(self, tasa):
        self.saldoInicial += self.saldoInicial * (tasa / 100)
        return self.saldoInicial

    def previsionAnual(self, tasa, anios=1):
        saldo = self.saldoInicial
        for _ in range(anios):
            saldo += saldo * (tasa / 100)
        return saldo