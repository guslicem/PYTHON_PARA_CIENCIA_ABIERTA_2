---
name: course-learner
description: Analiza, unifica e indexa materiales docentes existentes en FULL_COURSE_CSIC y FULL_COURSE_USE (eliminando redundancias, fusionando enfoques y priorizando el material más reciente de USE para un nuevo curso dirigido al CSIC), generando cuadernos estructurados en NOTEBOOKS/WIP/.
---
# Skill: Aprendizaje, Unificación y Generación de Cursos desde Materiales Previos

## Propósito

Dotar al agente de la capacidad de procesar de forma inteligente y recursiva los directorios de contenido docente `FULL_COURSE_CSIC/` y `FULL_COURSE_USE/`. El agente debe identificar redundancias, priorizar y fusionar las mejoras del material más reciente (USE) con el fondo base (CSIC), procesar los PDFs de presentaciones (`FULL_COURSE_USE/PDFS/` y `FULL_COURSE_CSIC/SCHEMA_AND_TIMING/`) para generar nuevos manuales docentes en PDF mejorados, y estructurar un nuevo temario de **20 Horas (5 Días de 4 Horas cada uno)** alojado en `NOTEBOOKS/WIP/`.

---

## Directivas de Ejecución

### 1. Ingesta, Análisis y Elevación del Estándar Didáctico

Cuando se solicite aprender o basarse en los cursos previos, el agente ejecutará los siguientes pasos:

- **Exploración de Directorios:** Recorrer de forma recursiva `FULL_COURSE_CSIC/` y `FULL_COURSE_USE/` localizando todos los archivos `.ipynb`, `.py`, documentos de texto y transparencias en PDF (`FULL_COURSE_USE/PDFS/`).
- **Extracción e Ingesta Teórica desde PDFs de Presentaciones:**
  - Extraer los esquemas conceptuales, explicaciones y temporizaciones de los PDFs de diapositivas (`0_Ejemplo_TITANIC.pdf`, `1_Intro_Tipos_Datos.pdf`, `2_Estructuras_de_Datos.pdf`, `3_Scripts_Y_Funciones.pdf`, `4_Control_de_Flujo.pdf`, `5_Intro_a_POO.pdf`, `6_Intro_a_Numpy.pdf`).
  - Utilizar este conocimiento para generar **nuevos manuales docentes en PDF** (`fpdf2`) side-by-side para el alumnado.
- **Análisis de Redundancias, Fusión y Elevación del Nivel:**
  - Integrar la frescura pedagógica de `FULL_COURSE_USE` con la especialización investigadora de `FULL_COURSE_CSIC`.
  - **Superación del Material Base:** El contenido generado debe elevar la calidad técnica respecto al material previo, incorporando tipado explícito (`typing`), docstrings detallados, manejo elegante de excepciones y mejores prácticas de Python 3.13.
- **Uso de Handles Reales de Digital.CSIC:**
  - Incorporar funciones de ingesta y resolución de registros mediante **handles reales de Digital.CSIC** (`http://hdl.handle.net/10261/...`).
- **Pedagogía de Corrupción y Curación de Datasets:**
  - Generar escenarios prácticos donde los datasets de metadatos del CSIC son intencionadamente corrompidos de forma realista (DOIs incompletos, fechas heterogéneas, espacios redundantes, codificación y nulos disimulados).
  - Guiar al alumnado en la limpieza, transformación, normalización y validación asistida por Pandas, Regex y herramientas de IA.
- **Indización Conceptual:** Generar y mantener actualizado el índice de referencia unificado en `artifacts/source_index.md`.

### 2. Estructuración del Curso en 20 Horas (Día a Día en Subcarpetas `NOTEBOOKS/WIP/DAYX/`)

El temario se distribuirá estrictamente día por día en subcarpetas dedicadas dentro de `NOTEBOOKS/WIP/`:

- **Estructura de Directorios:** `NOTEBOOKS/WIP/DAY1/`, `NOTEBOOKS/WIP/DAY2/`, `NOTEBOOKS/WIP/DAY3/`, `NOTEBOOKS/WIP/DAY4/`, `NOTEBOOKS/WIP/DAY5/`.
- **Enfoque Didáctico y Rigor Sin Resumir (REGLA FUNDAMENTAL):**
  - **Prohibido resumir o comprimir superficialmente:** Los cuadernos deben conservar toda la amplitud, tablas explicativas, avisos didácticos ("bájate de la atalaya"), celdas de código paso a paso y ejercicios de los cuadernos originales del CSIC, mejorando y ampliando los ejemplos con el material de USE.
  - **Adaptación Didáctica de POO (Día 2):** Diseñar la Programación Orientada a Objetos desde cero pensando en personal investigador y técnico del CSIC (muchos sin experiencia previa en programación). Evitar abstracciones ingenieriles complejas y utilizar clases intuitivas del entorno científico (`Muestra`, `Experimento`, `Publicacion`).

Distribución Diaria (5 Días x 4 Horas):
- **Día 1 (`NOTEBOOKS/WIP/DAY1/`) [4h]:** Setup de entorno (Antigravity-IDE, venv, Git, Pylance), Ejemplo Titanic y Fundamentos de Programación (Tipos Primitivos, Colecciones y Control de Flujo extensos).
- **Día 2 (`NOTEBOOKS/WIP/DAY2/`) [4h]:** Funciones avanzadas, POO Científica desde cero (Muestra, Experimento) y Computación Vectorial con **NumPy**.
- **Día 3 (`NOTEBOOKS/WIP/DAY3/`) [4h]:** Análisis Exploratorio de Datos con **Pandas**, Corrupción Simulada de Datasets y Técnicas Profesionales de Curación de Datos.
- **Día 4 (`NOTEBOOKS/WIP/DAY4/`) [4h]:** Visualización Científica con Matplotlib/Seaborn, Ingesta de **Digital.CSIC** por Handles, APIs REST, Web Scraping y Asistencia de Código con IA / Agentes Autónomos.
- **Día 5 (`NOTEBOOKS/WIP/DAY5/`) [4h]: Proyecto Integrador Colaborativo en Equipos con Git & GitHub.**

### 3. Ciclo de Vida de Cuadernos y Generación de PDFs (`fpdf2` / `nbclient`)

Para cada jornada del curso, los scripts de construcción (`_build_dayX.py`) deben ejecutar de forma automatizada los siguientes **5 pasos obligatorios**:

1. **Creación del Cuaderno (.ipynb):** Construir el cuaderno Jupyter con celdas teóricas Markdown y celdas de código Python.
2. **Ejecución Programática:** Ejecutar programáticamente el cuaderno completo con `nbclient` utilizando el kernel del entorno virtual `./venv/bin/python`.
3. **Guardado Transitorio:** Guardar el cuaderno `.ipynb` con todas sus salidas (`outputs`) de ejecución generadas.
4. **Exportación a PDF del Cuaderno Ejecutado (`XX_nombre_guia_y_ejecucion.pdf`):** Generar un documento PDF que combine el **resumen ejecutivo** de la lección con el **código completo y el resultado exacto de ejecución de cada celda**.
5. **Limpieza de Salidas y Guardado Final:** Borrar todas las salidas de ejecución del cuaderno (`cell.outputs = []`, `cell.execution_count = None`) y **guardar de nuevo el cuaderno `.ipynb` limpio**, listo para que el alumnado trabaje sobre él.

Además, para cada jornada se generará el PDF de **Resumen Ejecutivo del Día (`XX_resumen_ejecutivo_diaX.pdf`)**.

### Reglas Visuales y Técnicas Obligatorias para los PDFs:
- **Logo Banner Ancho Completo (190 mm):** En la portada de la primera página de cada PDF, incluir el logo oficial `assets/LogoCurso_gemini.png` ocupando todo el ancho imprimible (`w=190`).
- **Posicionamiento Vertical Seguro (`set_y(92)`):** Ajustar la coordenada `pdf.set_y(92)` inmediatamente después de imprimir la imagen para garantizar un margen limpio de 17 mm antes de los títulos, impidiendo cualquier solapamiento de texto sobre el logo.
- **Prohibición de `assert`:** No incluir comprobaciones `assert` en las celdas mostradas al alumnado; utilizar salidas limpias `print(f"...")`.
- **Ruta de Datasets:** Todas las llamadas a datos se realizarán buscando la carpeta `DATASETS/` en la raíz mediante resolución dinámica multinivel.

### 4. Ubicación, Limpieza y Trazabilidad

- **Ubicación Obligatoria:** Todos los cuadernos Jupyter (`.ipynb`) y manuales `.pdf` generados deben guardarse estrictamente en la subcarpeta del día correspondiente (ej. `NOTEBOOKS/WIP/DAY1/`).
- **Ruta Relativa del Logo en Notebooks:** La carpeta `assets/` está **siempre en la raíz del proyecto**. En `NOTEBOOKS/WIP/DAY1/` (3 niveles de profundidad), la ruta debe ser exactamente:
  `![Logo Curso](../../../assets/LogoCurso_gemini.png)`
- **Scripts de Construcción Reutilizables:** Conservar en cada subcarpeta el script ejecutable de compilación `_build_day1.py`, `_build_day2.py`, etc.
- **Trazabilidad:** Registrar las unificaciones y avances en `artifacts/changelog.md` y sincronizar exactamente con `CHANGELOG.md` y `README.md`.

---

## Restricciones Técnicas

- No modificar las restricciones de versiones en `requirements.txt`.
- Nunca escribir API keys ni credenciales directamente en los cuadernos ni scripts (`.env`).
