# Metadatos del Proyecto linuxitOS

En esta carpeta (`datos/`) guardamos todos los datasets utilizados en crudo y procesados. Cada archivo tiene su propia metadata descrita a continuación, cumpliendo con los lineamientos de la rúbrica del Módulo A.

---

### 1. Contexto Nacional y Estatal (Agenda 2030)
- **Nombre de archivo:** `siods_agua_saneamiento_nacional.csv`
- **Descripción de las variables (Data Dictionary):** 
  - `Indicador`: Nombre de la meta oficial (6.1.1.a Nacional o 6.1.1.c Estatal).
  - `Clave_Entidad`: Clave geoestadística de la zona (00 para Nacional, 01-32 para Estatal).
  - `Entidad`: Nombre geográfico.
  - `Año`: Año del registro (2020).
  - `Valor`: Porcentaje de cobertura del servicio.
- **Fuente:** Sistema de Información de los Objetivos de Desarrollo Sostenible (SIODS). API Oficial [Indicador 54 (Nacional)](https://agenda2030.mx/ODSind.html?ind=ODS006000050010&cveind=54&cveCob=99&lang=es#/Indicator) y [Indicador 618 (Estatal)](https://agenda2030.mx/ODSind.html?ind=ODS006000050030&cveind=618&cveCob=99&lang=es#/Indicator).
- **Fecha de descarga:** 02 de abril de 2026.
- **Licencia:** [Licencia de Código Abierto del Gobierno de México](https://www.agenda2030.mx/docs/doctos/system/Licencia_codigo_abierto_ES.pdf).

### 2. Geografía de la Desigualdad (Demografía INEGI)
- **Nombre de archivo:** Archivos dentro de la carpeta `iter_00_cpv2020_csv/`
- **Descripción de las variables (Data Dictionary):** 
  - `ENTIDAD`: Clave del Estado.
  - `MUN`: Clave del Municipio.
  - `LOC`: Clave de la Localidad.
  - `POBTOT`: Población total residente en esa localidad. *(Variable clave usada para determinar ruralidad: localidades < 2500 habitantes)*.
- **Fuente:** INEGI. Censo de Población y Vivienda 2020. Principales resultados por localidad (ITER). [Enlace de descarga oficial](https://www.inegi.org.mx/app/descarga/ficha.html?tit=326108&ag=0&f=csv)
- **Fecha de descarga:** 02 de abril de 2026.
- **Licencia:** [Términos de Libre Uso de la Información del INEGI](https://www.inegi.org.mx/contenidos/inegi/doc/terminos_sitio.pdf).

### 3. Dimensión de la Pobreza y Carencia de Infraestructura (CONEVAL)
- **Nombre de archivo:** `Concentrado_indicadores_de_pobreza_2020.xlsx` (y su versión limpia `coneval_clean_2020.csv`)
- **Descripción de las variables (Data Dictionary):** 
  - `CVEGEO`: Clave geográfica municipal (5 dígitos).
  - `Municipio`: Nombre del municipio.
  - `Pobreza_pct`: Porcentaje de la población en pobreza multidimensional.
  - `Pobreza_extrema_pct`: Porcentaje de la población en pobreza extrema.
  - `Carencia_servicios_pct`: Porcentaje de la población con carencia por acceso a los servicios básicos en la vivienda (Indicador oficial que penaliza la falta de agua y drenaje).
- **Fuente:** CONEVAL. Medición de la Pobreza a Nivel Municipal 2020. Anexo Estadístico. [Descarga ZIP original](https://www.coneval.org.mx/Medicion/Documents/Pobreza_municipal/2020/Concentrado_indicadores_de_pobreza_2020.zip)
- **Fecha de descarga:** 02 de abril de 2026 (Archivo original data de Dic 2021).
- **Licencia:** Libre Uso (Datos Abiertos del Gobierno de México / CONEVAL).

### 4. Dataset Maestro (Elaboración Propia)
- **Nombre de archivo:** `final_merged_data.csv`
- **Descripción de las variables (Data Dictionary):** Unificación de los microdatos del INEGI y CONEVAL. Incluye las variables de pobreza ya mencionadas, más el cálculo propio de ruralidad:
  - `poblacion_total`: Sumatoria de habitantes del municipio.
  - `pct_rural`: Porcentaje matemático de población viviendo en localidades < 2500 habs.
  - `clasificacion_rural`: Etiqueta categórica (`Rural` o `Urbano`) basada en si el `pct_rural` > 50%.
- **Fuente:** Elaboración propia (Equipo linuxitOS) con base en cruces de datos abiertos del INEGI (ITER) y CONEVAL.
- **Fecha de generación:** 02 de abril de 2026.
- **Licencia:** CC BY-SA 4.0 (Licencia general de este repositorio).
