import subprocess
import sys
import os

def run_script(script_path):
    print(f"\n{'-'*50}")
    print(f"[INFO] Ejecutando módulo: {script_path}")
    print(f"{'-'*50}")
    try:
        # Usar subprocess para llamar al script de python
        result = subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Falla en la ejecución de {script_path}. Abortando pipeline.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[FATAL] Error inesperado en el módulo {script_path}: {e}")
        sys.exit(1)

def main():
    print("Iniciando Pipeline Automatizado de Datos (ETL): HackODS UNAM 2026 - linuxitOS\n")
    
    # Asegurar el contexto de ejecución desde el directorio raíz
    if not os.path.exists('scripts'):
         print("[ERROR] El script debe ser invocado desde la raíz del repositorio (linuxitOS-HackODS2026)")
         sys.exit(1)

    # Orden secuencial de ejecución para la integración del dataset maestro
    pipeline = [
        "scripts/siods_extractor.py",
        "scripts/analyze_iter.py",
        "scripts/clean_coneval.py",
        "scripts/merge_inegi_coneval.py",
        "scripts/merge_shcp.py",
        "scripts/merge_conagua.py",
        "scripts/simplify_geojson.py"
    ]

    for script in pipeline:
        run_script(script)

    print("\n[ÉXITO] Pipeline ETL concluido satisfactoriamente.")
    print("[INFO] El dataset analítico 'final_merged_data.csv' ha sido generado exitosamente.")
    print("[INFO] Para compilar el dashboard Quarto, ejecute el siguiente comando:")
    print("       quarto render dashboard/index.qmd")

if __name__ == "__main__":
    main()
