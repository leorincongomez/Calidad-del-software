class CalculadoraBasica:

    def sumar(self, numero1, numero2):
        return numero1 + numero2

    def restar(self, numero1, numero2):
        return numero1 - numero2


class CalculadoraAreaCuadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado

    def calcularPerimetro(self):
        return 4 * self.lado


class ConversorTemperatura:

    def __init__(self, celsius):
        self.celsius = celsius

    def aFahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def aKelvin(self):
        return self.celsius + 273.15


class EstadisticaSimple:

    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calcularPromedio(self):
        return (self.num1 + self.num2 + self.num3) / 3


class CalculadoraIVA:

    def __init__(self, precioBase):
        self.precioBase = precioBase

    def obtenerIVA(self):
        return self.precioBase * 0.21

    def precioTotal(self):
        return self.precioBase + self.obtenerIVA()


class OperacionesPotencia:

    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcularPotencia(self):
        resultado = 1

        for i in range(self.exponente):
            resultado = resultado * self.base

        return resultado

    def calcularCuadrado(self):
        return self.base * self.base


class CalculadoraDescuentos:

    def __init__(self, precio, porcentaje):
        self.precio = precio
        self.porcentaje = porcentaje

    def montoDescuento(self):
        return self.precio * self.porcentaje / 100

    def precioFinal(self):
        return self.precio - self.montoDescuento()


class GeometriaCirculo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def circunferencia(self):
        return 2 * 3.1416 * self.radio


class ConvertidorMedidas:

    def __init__(self, metros):
        self.metros = metros

    def aCentimetros(self):
        return self.metros * 100

    def aKilometros(self):
        return self.metros / 1000


class CalculadoraTriangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2


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


class CalculadoraIMC:

    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def obtenerIndice(self):
        return self.peso / (self.altura ** 2)


class RepartidorGastos:

    def __init__(self, totalFactura, numeroPersonas):
        self.totalFactura = totalFactura
        self.numeroPersonas = numeroPersonas

    def divisionEquitativa(self):
        return self.totalFactura / self.numeroPersonas


class CalculadoraVelocidad:

    def __init__(self, distancia, tiempo):
        self.distancia = distancia
        self.tiempo = tiempo

    def calcularVelocidadMedia(self):
        return self.distancia / self.tiempo


class AnalisisNumerico:

    def __init__(self, numero):
        self.numero = numero

    def esPar(self):
        return self.numero % 2 == 0

    def obtenerDoble(self):
        return self.numero * 2


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


class CalculadoraSalario:

    def __init__(self, salarioBase, horasExtra):
        self.salarioBase = salarioBase
        self.horasExtra = horasExtra

    def calcularPagoExtra(self):
        return self.horasExtra * 10

    def calcularSalarioTotal(self):
        return self.salarioBase + self.calcularPagoExtra()


class CalculadoraCombustible:

    def __init__(self, distancia, consumo_por_km):
        self.distancia = distancia
        self.consumo_por_km = consumo_por_km

    def calcularCombustibleNecesario(self):
        return self.distancia * self.consumo_por_km

    def calcularCostoViaje(self, precio_litro):
        litros_necesarios = self.calcularCombustibleNecesario()
        return litros_necesarios * precio_litro


class CalculadoraDistancia:

    def __init__(self, distanciaInicial, distanciaFinal):
        self.distanciaInicial = distanciaInicial
        self.distanciaFinal = distanciaFinal

    def calcularDistancia(self):
        return self.distanciaFinal - self.distanciaInicial


class CalculadoraInteres:

    def __init__(self, capital, tasa, tiempo):
        self.capital = capital
        self.tasa = tasa
        self.tiempo = tiempo

    def calcularInteres(self):
        return self.capital * (self.tasa / 100) * self.tiempo

    def calcularMonto(self):
        return self.capital + self.calcularInteres()


class CalculadoraPropina:

    def __init__(self, total, porcentaje):
        self.total = total
        self.porcentaje = porcentaje

    def calcularPropina(self):
        return self.total * self.porcentaje / 100

    def calcularTotal(self):
        return self.total + self.calcularPropina()


# =========================================================
# FUNCIONES PARA PROBAR CADA CLASE
# =========================================================

def probarCalculadoraBasica():

    print("\n--- CALCULADORA BÁSICA ---")

    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    calculadora = CalculadoraBasica()

    print("Suma:", calculadora.sumar(numero1, numero2))
    print("Resta:", calculadora.restar(numero1, numero2))


def probarAreaCuadrado():

    print("\n--- ÁREA Y PERÍMETRO DEL CUADRADO ---")

    lado = float(input("Ingrese el lado del cuadrado: "))

    cuadrado = CalculadoraAreaCuadrado(lado)

    print("Área:", cuadrado.calcularArea())
    print("Perímetro:", cuadrado.calcularPerimetro())


def probarTemperatura():

    print("\n--- CONVERSOR DE TEMPERATURA ---")

    celsius = float(input("Ingrese la temperatura en Celsius: "))

    temperatura = ConversorTemperatura(celsius)

    print("Fahrenheit:", temperatura.aFahrenheit())
    print("Kelvin:", temperatura.aKelvin())


def probarEstadistica():

    print("\n--- ESTADÍSTICA SIMPLE ---")

    num1 = float(input("Ingrese el número 1: "))
    num2 = float(input("Ingrese el número 2: "))
    num3 = float(input("Ingrese el número 3: "))

    estadistica = EstadisticaSimple(num1, num2, num3)

    print("Promedio:", estadistica.calcularPromedio())


def probarIVA():

    print("\n--- CALCULADORA IVA ---")

    precio = float(input("Ingrese el precio base: "))

    calculadora = CalculadoraIVA(precio)

    print("IVA (21%):", calculadora.obtenerIVA())
    print("Precio total:", calculadora.precioTotal())


def probarPotencia():

    print("\n--- OPERACIONES DE POTENCIA ---")

    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))

    operacion = OperacionesPotencia(base, exponente)

    print("Potencia:", operacion.calcularPotencia())
    print("Cuadrado:", operacion.calcularCuadrado())


def probarDescuentos():

    print("\n--- CALCULADORA DE DESCUENTOS ---")

    precio = float(input("Ingrese el precio: "))
    porcentaje = float(input("Ingrese el porcentaje de descuento: "))

    descuento = CalculadoraDescuentos(precio, porcentaje)

    print("Monto del descuento:", descuento.montoDescuento())
    print("Precio final:", descuento.precioFinal())


def probarCirculo():

    print("\n--- GEOMETRÍA DEL CÍRCULO ---")

    radio = float(input("Ingrese el radio: "))

    circulo = GeometriaCirculo(radio)

    print("Área:", circulo.area())
    print("Circunferencia:", circulo.circunferencia())


def probarMedidas():

    print("\n--- CONVERTIDOR DE MEDIDAS ---")

    metros = float(input("Ingrese los metros: "))

    convertidor = ConvertidorMedidas(metros)

    print("Centímetros:", convertidor.aCentimetros())
    print("Kilómetros:", convertidor.aKilometros())


def probarTriangulo():

    print("\n--- ÁREA DEL TRIÁNGULO ---")

    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))

    triangulo = CalculadoraTriangulo(base, altura)

    print("Área:", triangulo.calcularArea())


def probarAhorro():

    print("\n--- AHORRO PERSONAL ---")

    saldo = float(input("Ingrese el saldo inicial: "))
    tasa = float(input("Ingrese la tasa de interés (%): "))
    anios = int(input("Ingrese los años: "))

    ahorro = AhorroPersonal(saldo)

    print("Saldo después de agregar interés:",
          ahorro.agregarInteres(tasa))

    print("Previsión anual:",
          ahorro.previsionAnual(tasa, anios))


def probarIMC():

    print("\n--- CALCULADORA IMC ---")

    peso = float(input("Ingrese el peso en kg: "))
    altura = float(input("Ingrese la altura en metros: "))

    imc = CalculadoraIMC(peso, altura)

    print("Índice de masa corporal:", imc.obtenerIndice())


def probarGastos():

    print("\n--- REPARTIDOR DE GASTOS ---")

    factura = float(input("Ingrese el total de la factura: "))
    personas = int(input("Ingrese el número de personas: "))

    gastos = RepartidorGastos(factura, personas)

    print("Cada persona debe pagar:",
          gastos.divisionEquitativa())


def probarVelocidad():

    print("\n--- CALCULADORA DE VELOCIDAD ---")

    distancia = float(input("Ingrese la distancia en km: "))
    tiempo = float(input("Ingrese el tiempo en horas: "))

    velocidad = CalculadoraVelocidad(distancia, tiempo)

    print("Velocidad media:",
          velocidad.calcularVelocidadMedia(), "km/h")


def probarAnalisis():

    print("\n--- ANÁLISIS NUMÉRICO ---")

    numero = int(input("Ingrese un número: "))

    analisis = AnalisisNumerico(numero)

    print("¿Es par?:", analisis.esPar())
    print("Doble:", analisis.obtenerDoble())


def probarFactura():

    print("\n--- CALCULADORA DE FACTURA ---")

    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    descuento = float(input("Ingrese el descuento (%): "))

    factura = CalculadoraFactura(precio, cantidad, descuento)

    print("Subtotal:", factura.calcularSubtotal())
    print("Descuento:", factura.calcularDescuento())
    print("Total:", factura.calcularTotal())


def probarSalario():

    print("\n--- CALCULADORA DE SALARIO ---")

    salarioBase = float(input("Ingrese el salario base: "))
    horasExtra = int(input("Ingrese las horas extra: "))

    salario = CalculadoraSalario(salarioBase, horasExtra)

    print("Pago por horas extra:",
          salario.calcularPagoExtra())

    print("Salario total:",
          salario.calcularSalarioTotal())


def probarCombustible():

    print("\n--- CALCULADORA DE COMBUSTIBLE ---")

    distancia = float(input("Ingrese la distancia del viaje en km: "))
    consumo = float(input("Ingrese el consumo de combustible por km: "))
    precio = float(input("Ingrese el precio por litro: "))

    combustible = CalculadoraCombustible(distancia, consumo)

    print("Combustible necesario:",
          combustible.calcularCombustibleNecesario())

    print("Costo del viaje:",
          combustible.calcularCostoViaje(precio))


def probarDistancia():

    print("\n--- CALCULADORA DE DISTANCIA ---")

    inicial = float(input("Ingrese la distancia inicial: "))
    final = float(input("Ingrese la distancia final: "))

    distancia = CalculadoraDistancia(inicial, final)

    print("Distancia recorrida:",
          distancia.calcularDistancia())


def probarInteres():

    print("\n--- CALCULADORA DE INTERÉS ---")

    capital = float(input("Ingrese el capital: "))
    tasa = float(input("Ingrese la tasa de interés (%): "))
    tiempo = float(input("Ingrese el tiempo en años: "))

    interes = CalculadoraInteres(capital, tasa, tiempo)

    print("Interés generado:",
          interes.calcularInteres())

    print("Monto final:",
          interes.calcularMonto())


def probarPropina():

    print("\n--- CALCULADORA DE PROPINA ---")

    total = float(input("Ingrese el total de la cuenta: "))
    porcentaje = float(input("Ingrese el porcentaje de propina: "))

    propina = CalculadoraPropina(total, porcentaje)

    print("Propina:",
          propina.calcularPropina())

    print("Total con propina:",
          propina.calcularTotal())


# =========================================================
# MENÚ PRINCIPAL
# =========================================================

def mostrarMenu():

    print("\n")
    print("=" * 50)
    print("        MENÚ DE EJERCICIOS PYTHON")
    print("=" * 50)

    print("1.  Calculadora Básica")
    print("2.  Área y Perímetro del Cuadrado")
    print("3.  Conversor de Temperatura")
    print("4.  Estadística Simple")
    print("5.  Calculadora IVA")
    print("6.  Operaciones de Potencia")
    print("7.  Calculadora de Descuentos")
    print("8.  Geometría del Círculo")
    print("9.  Convertidor de Medidas")
    print("10. Calculadora de Triángulo")
    print("11. Ahorro Personal")
    print("12. Calculadora IMC")
    print("13. Repartidor de Gastos")
    print("14. Calculadora de Velocidad")
    print("15. Análisis Numérico")
    print("16. Calculadora de Factura")
    print("17. Calculadora de Salario")
    print("18. Calculadora de Combustible")
    print("19. Calculadora de Distancia")
    print("20. Calculadora de Interés")
    print("21. Calculadora de Propina")

    print("-" * 50)
    print("22. EJECUTAR TODAS")
    print("0.  SALIR")
    print("=" * 50)


def ejecutarOpcion(opcion):

    if opcion == 1:
        probarCalculadoraBasica()

    elif opcion == 2:
        probarAreaCuadrado()

    elif opcion == 3:
        probarTemperatura()

    elif opcion == 4:
        probarEstadistica()

    elif opcion == 5:
        probarIVA()

    elif opcion == 6:
        probarPotencia()

    elif opcion == 7:
        probarDescuentos()

    elif opcion == 8:
        probarCirculo()

    elif opcion == 9:
        probarMedidas()

    elif opcion == 10:
        probarTriangulo()

    elif opcion == 11:
        probarAhorro()

    elif opcion == 12:
        probarIMC()

    elif opcion == 13:
        probarGastos()

    elif opcion == 14:
        probarVelocidad()

    elif opcion == 15:
        probarAnalisis()

    elif opcion == 16:
        probarFactura()

    elif opcion == 17:
        probarSalario()

    elif opcion == 18:
        probarCombustible()

    elif opcion == 19:
        probarDistancia()

    elif opcion == 20:
        probarInteres()

    elif opcion == 21:
        probarPropina()

    elif opcion == 22:
        ejecutarTodas()

    else:
        print("Opción no válida.")


def pausar():

    input("\nPresione ENTER para volver al menú...")


def ejecutarTodas():

    print("\n")
    print("=" * 50)
    print("       EJECUTANDO TODOS LOS EJERCICIOS")
    print("=" * 50)

    probarCalculadoraBasica()
    pausar()

    probarAreaCuadrado()
    pausar()

    probarTemperatura()
    pausar()

    probarEstadistica()
    pausar()

    probarIVA()
    pausar()

    probarPotencia()
    pausar()

    probarDescuentos()
    pausar()

    probarCirculo()
    pausar()

    probarMedidas()
    pausar()

    probarTriangulo()
    pausar()

    probarAhorro()
    pausar()

    probarIMC()
    pausar()

    probarGastos()
    pausar()

    probarVelocidad()
    pausar()

    probarAnalisis()
    pausar()

    probarFactura()
    pausar()

    probarSalario()
    pausar()

    probarCombustible()
    pausar()

    probarDistancia()
    pausar()

    probarInteres()
    pausar()

    probarPropina()
    pausar()

    print("\n")
    print("=" * 50)
    print("       TERMINARON TODOS LOS EJERCICIOS")
    print("=" * 50)


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

while True:

    mostrarMenu()

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 0:
            print("\nPrograma finalizado.")
            break

        ejecutarOpcion(opcion)

        if opcion != 22:
            pausar()

    except ValueError:
        print("\nDebe ingresar un número válido.")