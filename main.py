import os
import sys
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

# Configurar encoding UTF-8 para la consola en Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def discover_exercises():
    """
    Escanea la carpeta del proyecto en busca de directorios de ejercicios.
    Retorna un diccionario {numero_ejercicio: [(dir_path, test_file_path), ...]}
    """
    exercises = {}
    
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        dir_name = os.path.basename(root)
        match = re.search(r'ejercicio[_\-]?(\d+)', dir_name, re.IGNORECASE)
        
        if match:
            num = int(match.group(1))
            test_files = [f for f in files if f.startswith('test') and f.endswith('.py')]
            if not test_files:
                test_files = [f for f in files if f.endswith('.py') and ('test' in f.lower())]
            
            for tf in test_files:
                tf_path = os.path.join(root, tf)
                if num not in exercises:
                    exercises[num] = []
                exercises[num].append((root, tf_path))
                
    return dict(sorted(exercises.items()))

def run_single_test(root_dir, test_file):
    """
    Ejecuta un archivo de prueba individual utilizando subprocess en su propio directorio.
    """
    rel_dir = os.path.relpath(root_dir, BASE_DIR)
    test_basename = os.path.basename(test_file)
    start_time = time.time()
    
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    result = subprocess.run(
        [sys.executable, "-m", "unittest", test_basename],
        cwd=root_dir,
        capture_output=True,
        text=True,
        env=env,
        encoding='utf-8',
        errors='replace'
    )
    
    elapsed = time.time() - start_time
    success = (result.returncode == 0)
    output = result.stdout + result.stderr
    
    return {
        "dir": rel_dir,
        "file": test_basename,
        "success": success,
        "output": output,
        "elapsed": elapsed
    }

def run_exercise_tests(num, exercises_dict):
    """
    Ejecuta las pruebas de un ejercicio específico.
    """
    if num not in exercises_dict:
        print(f"\n[ERROR] El ejercicio #{num} no fue encontrado o no tiene pruebas configuradas.")
        print(f"Ejercicios disponibles: {list(exercises_dict.keys())}")
        return False

    tests = exercises_dict[num]
    print(f"\n==========================================")
    print(f"  EJECUTANDO PRUEBAS: EJERCICIO {num}")
    print(f"==========================================")
    
    all_success = True
    for root_dir, test_file in tests:
        rel_file = os.path.relpath(test_file, BASE_DIR)
        print(f"\n--> Corriendo: {rel_file}")
        res = run_single_test(root_dir, test_file)
        
        print(res["output"].strip())
        status = "[EXITOSO]" if res["success"] else "[FALLIDO]"
        print(f"Resultado: {status} ({res['elapsed']:.2f}s)\n")
        
        if not res["success"]:
            all_success = False
            
    return all_success

def run_all_tests_simultaneously(exercises_dict):
    """
    Ejecuta todos los tests de todos los ejercicios simultáneamente utilizando concurrencia.
    """
    print(f"\n==================================================")
    print(f"  EJECUTANDO TODOS LOS EJERCICIOS SIMULTÁNEAMENTE  ")
    print(f"==================================================")
    
    tasks = []
    for num, tests in exercises_dict.items():
        for root_dir, test_file in tests:
            tasks.append((num, root_dir, test_file))
            
    start_total = time.time()
    results = []
    
    with ThreadPoolExecutor(max_workers=min(len(tasks), 10)) as executor:
        futures = {
            executor.submit(run_single_test, root_dir, test_file): (num, root_dir, test_file)
            for num, root_dir, test_file in tasks
        }
        
        for future in futures:
            num, root_dir, test_file = futures[future]
            res = future.result()
            res["num"] = num
            results.append(res)
            
    total_elapsed = time.time() - start_total
    
    print("\n------------------- DETALLE DE RESULTADOS -------------------")
    results.sort(key=lambda x: (x["num"], x["file"]))
    
    total_passed = 0
    total_failed = 0
    
    for res in results:
        status_symbol = "[PASÓ]" if res["success"] else "[FALLÓ]"
        if res["success"]:
            total_passed += 1
        else:
            total_failed += 1
            
        print(f"\n[Ejercicio #{res['num']}] Folder: {res['dir']} | Archivo: {res['file']} --> {status_symbol}")
        if res["output"].strip():
            indented = "   " + "\n   ".join(res["output"].strip().splitlines())
            print(indented)
            
    print("\n==================================================")
    print("                RESUMEN DE EJECUCIÓN              ")
    print("==================================================")
    print(f" Total de suites de pruebas ejecutadas: {len(results)}")
    print(f"  - Pasaron:  {total_passed}")
    print(f"  - Fallaron: {total_failed}")
    print(f" Tiempo total de ejecución simultánea: {total_elapsed:.2f} segundos")
    print("==================================================\n")

def main():
    exercises = discover_exercises()
    
    # Si se pasan argumentos por línea de comandos
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip().lower()
        if arg in ["todos", "all", "0"]:
            run_all_tests_simultaneously(exercises)
        elif arg.isdigit():
            run_exercise_tests(int(arg), exercises)
        else:
            print(f"Opción no reconocida: '{arg}'")
            print("Uso: python main.py [numero_ejercicio | todos]")
        return

    # Modo interactivo si no hay argumentos
    while True:
        print("\n==============================================")
        print("    MENÚ DE PRUEBAS DE EJERCICIOS (TALLER 2)  ")
        print("==============================================")
        print(" Ejercicios disponibles:")
        for num in exercises.keys():
            print(f"   [{num}] Ejercicio #{num}")
        print("\n Opciones especiales:")
        print("   [0] Ejecutar TODOS los ejercicios simultáneamente")
        print("   [q] Salir")
        print("----------------------------------------------")
        
        try:
            user_input = input("Ingrese el número del ejercicio a probar: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n¡Hasta luego!")
            break
            
        if user_input in ['q', 'salir', 'exit']:
            print("¡Hasta luego!")
            break
        elif user_input in ['0', 'todos', 'all']:
            run_all_tests_simultaneously(exercises)
        elif user_input.isdigit():
            num = int(user_input)
            run_exercise_tests(num, exercises)
        else:
            print("\n[!] Entrada inválida. Ingrese un número de ejercicio, '0' o 'todos'.")

if __name__ == "__main__":
    main()
