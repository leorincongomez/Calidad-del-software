class AnalisisNumerico:
    """
    Clase AnalisisNumerico
    Atributo: numero
    Métodos: esPar() -> retorna verdadero/falso
             obtenerDoble() -> retorna el doble del número
    """

    def __init__(self, numero):
        self.numero = numero

    def esPar(self):
        return self.numero % 2 == 0

    def obtenerDoble(self):
        return self.numero * 2


if __name__ == "__main__":
    an = AnalisisNumerico(8)
    print(f"Número: {an.numero}")
    print(f"¿Es par?: {an.esPar()}")
    print(f"Doble: {an.obtenerDoble()}")