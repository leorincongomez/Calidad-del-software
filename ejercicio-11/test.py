from ejercicio11 import AhorroPersonal
 
ahorro = AhorroPersonal(1000)
print("Saldo inicial:", ahorro.saldoInicial)
 
nuevo_saldo = ahorro.agregarInteres(10)
print("Saldo con interes:", nuevo_saldo)
 
prevision = ahorro.previsionAnual(10, 3)
print("Prevision a 3 años:", prevision)