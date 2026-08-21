from ejercicio18.calculadora_combustible import CalculadoraCombustible

print("\n--- Ejecutando Ejercicio 18: Calculadora de Combustible ---")
try:
    # Pidiendo datos interactivos para probar la funcionalidad
    distancia = float(input("Ingresa la distancia del viaje (km): "))
    consumo = float(input("Ingresa el consumo del vehículo (litros por km): "))
    precio = float(input("Ingresa el precio por litro de combustible ($): "))
    
    # Instanciando tu clase
    mi_viaje = CalculadoraCombustible(distancia, consumo)
    
    # Calculando y mostrando resultados
    print("\n--- Resultados del Viaje ---")
    print(f"Litros necesarios: {mi_viaje.calcularCombustibleNecesario():.2f} L")
    print(f"Costo total del viaje: ${mi_viaje.calcularCostoViaje(precio):.2f}")
except ValueError:
    print("Error: Por favor ingresa solo números válidos.")
print("-----------------------------------------------------------\n")