# linuxitOS - HackODS UNAM 2026

## Datos del equipo
- **Nombre del equipo:** linuxitOS
- **Integrantes:** 
  - Jesús Sebastián Vázquez Zarco
  - Alejandra Naomi Muciño Hernández
  - Victor Federico Caldera Arellano
- **ODS Elegidos:** ODS 6 (Agua limpia y saneamiento) interconectado con el ODS 1 (Fin de la pobreza).

## Descripción breve del proyecto
Este proyecto aborda el agua como un derecho humano y entiende la pobreza desde un enfoque multidimensional (la falta de servicios básicos indispensables para vivir dignamente). Su objetivo es visibilizar con datos cómo los déficits de abastecimiento castigan principalmente a las poblaciones rurales y vulnerables, demostrando que es imposible romper el ciclo de la pobreza sin infraestructura hídrica equitativa.

**Pregunta central:** ¿Cómo el déficit en la infraestructura de agua potable y saneamiento profundiza la pobreza multidimensional en las zonas rurales o periféricas frente a las zonas urbanas de México?

## Instrucciones de Reproducibilidad (Pipeline Técnico)
Para cumplir con el rigor de reproducibilidad técnica, todo el flujo de extracción y transformación de datos ha sido automatizado. Para replicarlo:

1. Clonar el repositorio y acceder a la carpeta:
   ```bash
   git clone <URL_DEL_REPO>
   cd linuxitOS-HackODS2026
   ```
2. Instalar las dependencias oficiales:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar los scripts en el siguiente orden:
   - `python scripts/siods_extractor.py` (Extrae métricas Nacionales/Estatales vía API).
   - `python scripts/analyze_iter.py` (Analiza ruralidad municipal con datos de INEGI).
   - `python scripts/clean_coneval.py` (Limpia datos de pobreza municipal).
   - `python scripts/merge_inegi_coneval.py` (Cruza los padrones y genera dataset final).
   - `python scripts/merge_shcp.py` (Integra datos de recaudación financiera y tomas pagadas).
4. Renderizar el Dashboard interactivo:
   ```bash
   quarto render dashboard/index.qmd
   ```

## Estructura del repositorio
- `datos/`: Almacenamiento de datasets en crudo y procesados.
- `scripts/`: Código y notebooks para extracción, limpieza y cruce de datos.
- `dashboard/`: Código fuente del tablero en Quarto (.qmd) y archivos de estilo (.css) para la visualización de resultados.

## Metadatos de los datos (En progreso)
*Por favor consultar el archivo `datos/README.md` para la descripción detallada de las fuentes, fechas de descarga, licencias y variables de cada dataset utilizado en el proyecto una vez que sean integrados.*

## Declaratoria de uso de IA
Para conocer el registro del uso de herramientas de Inteligencia Artificial en el desarrollo de este proyecto, por favor revisar el archivo `ai-log.md`.

## Licencia
El contenido de este proyecto se comparte bajo la Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0).
