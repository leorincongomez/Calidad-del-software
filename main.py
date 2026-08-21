import os
import sys
import unittest


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def ejecutar_pruebas_directorio(directorio, nombre_ejercicio):
    print("\n" + "=" * 60)
    print(f" EJECUTANDO PRUEBAS: {nombre_ejercicio} ({directorio})")
    print("=" * 60 + "\n")

    abs_dir = os.path.abspath(directorio)
    if abs_dir not in sys.path:
        sys.path.insert(0, abs_dir)

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=abs_dir, pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "-" * 60)
    if result.wasSuccessful():
        print(f" RESULTADO: TODAS LAS PRUEBAS DE {nombre_ejercicio} PASARON EXITOSAMENTE.")
    else:
        print(f" RESULTADO: ALGUNAS PRUEBAS DE {nombre_ejercicio} FALLARON.")
    print("-" * 60 + "\n")
    return result.wasSuccessful()


def ejecutar_todas_las_pruebas(ejercicios):
    print("\n" + "=" * 60)
    print(" EJECUTANDO TODAS LAS PRUEBAS ")
    print("=" * 60)
    
    exitos = 0
    total = len(ejercicios)
    
    for clave, (nombre, directorio) in ejercicios.items():
        if os.path.exists(directorio):
            exito = ejecutar_pruebas_directorio(directorio, nombre)
            if exito:
                exitos += 1
        else:
            print(f"\n[!] El directorio '{directorio}' para '{nombre}' no existe.")

    print("\n" + "=" * 60)
    print(f" RESUMEN FINAL: {exitos}/{total} ejercicios pasaron todas sus pruebas.")
    print("=" * 60 + "\n")


def mostrar_menu(ejercicios):
    print("\n" + "=" * 50)
    print("      MENÚ DE EJECUCIÓN DE PRUEBAS DE SOFTWARE")
    print("=" * 50)
    print("Seleccione una opción:\n")
    
    for clave, (nombre, _) in ejercicios.items():
        print(f"  [{clave}] Pruebas del {nombre}")
    
    print("  [A] Ejecutar TODAS las pruebas")
    print("  [0] Salir")
    print("=" * 50)


def main():
    # Registro de ejercicios disponibles
    # Estructura: 'opcion': ('Nombre Visible', 'directorio')
    ejercicios = {
        "16": ("Ejercicio 16", "ejercicio-16"),
    }

    while True:
        mostrar_menu(ejercicios)
        opcion = input("Ingrese su opción: ").strip().upper()

        if opcion == "0":
            print("\n¡Hasta luego!")
            break
        elif opcion in ejercicios:
            nombre, directorio = ejercicios[opcion]
            if os.path.exists(directorio):
                ejecutar_pruebas_directorio(directorio, nombre)
            else:
                print(f"\n Error: El directorio '{directorio}' no existe.")
            input("Presione ENTER para continuar...")
        elif opcion == "A":
            ejecutar_todas_las_pruebas(ejercicios)
            input("Presione ENTER para continuar...")
        else:
            print("\n Opción no válida. Por favor, intente de nuevo.")
            input("Presione ENTER para continuar...")


if __name__ == "__main__":
    main()
