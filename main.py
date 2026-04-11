import subprocess
import sys
import os

def run_script(script_path):
    print(f"\n{'='*50}")
    print(f"🚀 Ejecutando: {script_path}")
    print(f"{'='*50}")
    try:
        # Usar subprocess para llamar al script de python
        result = subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error al ejecutar {script_path}. Deteniendo el pipeline.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado con {script_path}: {e}")
        sys.exit(1)

def main():
    print("Iniciando Pipeline Completo: HackODS UNAM 2026 - linuxitOS\n")
    
    # Asegurarnos de correr esto desde la raíz del proyecto
    if not os.path.exists('scripts'):
         print("❌ Error: Por favor, ejecuta este script desde la raíz del repositorio (linuxitOS-HackODS2026)")
         sys.exit(1)

    # Orden de ejecución para asegurar la correcta construcción del dataset final
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

    print("\n✅ ¡Pipeline ETL ejecutado exitosamente!")
    print("📈 El dataset maestro 'final_merged_data.csv' está listo para el Dashboard Quarto.")
    print("📝 Para renderizar el dashboard ejecuta: quarto render dashboard/index.qmd")

if __name__ == "__main__":
    main()
