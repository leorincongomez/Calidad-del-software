from RepartidorGastos import RepartidorGastos

gasto = RepartidorGastos(150000, 5)

resultado = gasto.divisionEquitativa()

print("Total de la factura:", gasto.totalFactura)
print("Número de personas:", gasto.numeroPersonas)
print("Valor que debe pagar cada persona:", resultado)