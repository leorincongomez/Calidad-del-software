from calculadora_triangulo import CalculadoraTriangulo

triangulo = CalculadoraTriangulo(base=6, altura=4)

area = triangulo.calcularArea()
print(f"Área del triángulo: {area}")

assert triangulo.calcularArea() == 12, "Error: el área no coincide"
print("Prueba exitosa")