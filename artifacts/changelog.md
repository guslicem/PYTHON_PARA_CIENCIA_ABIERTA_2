# Changelog del Curso

## [Inicialización] - 2026-08-05

### Añadido

- Configuración inicial de entorno y directivas de agente `.agents/AGENTS.md`.
- Especificación de la carpeta `NOTEBOOKS/` en la raíz para alojar los cuadernos del curso.
- Estructuración de directorio de artefactos (`artifacts/`) y directorio de skills (`.agents/skills/`).
- Creación de `requirements.txt` con librerías para Jupyter y análisis de datos.
- Asignación del rol principal: **Creador y Autor de Cursos de Python**.
- Generación del mapa conceptual y plan de unificación en `artifacts/source_index.md` mediante la habilidad `course-learner`, integrando `FULL_COURSE_CSIC` y `FULL_COURSE_USE`.

## [WIP - Módulo IA y Agentes] - 2026-08-05

### Añadido

- Creación de la habilidad `ai-coding-assistant-module` en `.agents/skills/ai-coding-assistant-module/SKILL.md`.
- Generación de cuadernos interactivos etiquetados como Trabajo en Progreso en `NOTEBOOKS/WIP/`:
  - `NOTEBOOKS/WIP/15_Autocompletado_Inteligente_con_IA.ipynb`: Guía práctica e interactiva paso a paso (*Comment-to-Code*, atajos `Tab`/`Ghost Text`, generación automática de docstrings con `"""`, refactorización con `Cmd+K` y depuración asistida "Fix with AI").
  - `NOTEBOOKS/WIP/16_Programacion_Basada_en_Agentes_Antigravity.ipynb`: Paradigma de agentes autónomos, ciclo ReAct, Tool Calling con Google GenAI / Antigravity SDK y evaluación con aserciones.
- Integración de la imagen del logo del curso (`assets/LogoCurso_gemini.png`) en el encabezado de los cuadernos.
- Incorporación de la regla 6 en `.agents/AGENTS.md` detallando las extensiones imprescindibles del IDE (incluyendo `google.gemini` / `google.antigravity`, `ms-python.python`, `ms-toolsai.jupyter`, `ms-toolsai.datawrangler`, `rainbow-csv`, `latex-workshop`) para la distribución del entorno al alumnado del CSIC.

## [Configuración IDE - Pylance y Autocompletado Cuadernos] - 2026-08-06

### Añadido
- Instalación de la extensión Pylance (`ms-python.vscode-pylance`) en el directorio de extensiones de Antigravity-IDE (`~/.antigravity-ide/extensions/`).
- Actualización de `.agents/AGENTS.md` incorporando la regla 7 con la configuración obligatoria de settings del IDE (`notebook.inlineSuggest.enabled`, `editor.inlineSuggest.enabled`, `python.languageServer: Pylance`).

## [Refactorización Módulo IA - Enfoque Módulos Python + PDF + Depuración] - 2026-08-06

### Cambiado
- Rediseño completo de la habilidad `ai-coding-assistant-module` en `.agents/skills/ai-coding-assistant-module/SKILL.md` para transicionar de celdas Jupyter a un **Flujo Dual (Módulos ejecutable Python `.py` + Guías PDF side-by-side + Arnés de Evaluación `.ipynb`)**.
- Incorporación de dependencias `fpdf2` y `markdown` en `requirements.txt` e instalación en `./venv` para automatizar la generación de manuales docentes PDF.
- Actualización de `artifacts/source_index.md` definiendo la nueva arquitectura del Módulo 15 y Módulo 16 orientada a la edición de scripts `.py` (donde *Ghost Text*, `Cmd+K` y la depuración con `F5`/breakpoints funcionan con total fiabilidad).

## [Actualización Skill IA y Limpieza de Auxiliares] - 2026-08-06

### Cambiado
- Integración de los detalles de ejecución de los Módulos 15 y 16 en `.agents/skills/ai-coding-assistant-module/SKILL.md`.
- Incorporación de la **Directiva de Limpieza Automatizada**: Instrucción explícita para que el agente elimine automáticamente todos los archivos Python auxiliares/temporales de generación y pruebas (`crear_*.py`, `generar_*.py`, `test.py`) al finalizar.
- Eliminación de scripts auxiliares en `NOTEBOOKS/WIP/`, dejando exclusivamente los 6 artefactos finales del curso (`.py`, `.pdf`, `.ipynb`).

## [Corrección Ruta del Logo en Cuadernos Jupyter] - 2026-08-06

### Corregido
- Corregida la ruta relativa de la imagen del logo del curso (`assets/LogoCurso_gemini.png`) en la celda inicial de los cuadernos en `NOTEBOOKS/WIP/` a `../../assets/LogoCurso_gemini.png` para referenciar correctamente la raíz del repositorio.
- Actualizada la Directiva 1 en `.agents/skills/ai-coding-assistant-module/SKILL.md` documentando explícitamente el cálculo de profundidad relativa hacia la carpeta `assets/` en la raíz.

## [Rediseño Avanzado Curso 20h - Ingesta Digital.CSIC, Corrupción de Datasets y Proyecto GitHub] - 2026-08-06

### Cambiado
- Rediseño estructural del temario completo para una duración total de **20 Horas (5 Días de 4 Horas cada uno)**.
- Actualización de `.agents/skills/course_learner/SKILL.md` especificando la elevación de estándar técnico, ingesta de metadatos por handles de Digital.CSIC y el patrón pedagógico de corrupción/curación de datos.
- Incorporación del **Proyecto Integrador Colaborativo en Equipos en GitHub** para el Día 5 (4h).
- Actualización completa del mapa conceptual e índice de fuentes en `artifacts/source_index.md`.

## [Generación Completa Temario 20h en NOTEBOOKS/WIP/] - 2026-08-06

### Añadido
- Generación de todos los cuadernos interactivos de Jupyter (`.ipynb`) del temario de 20 Horas (Días 1 a 5) en `NOTEBOOKS/WIP/`:
  - `00_Setup_y_Ejemplo_Inicial_Titanic.ipynb` y `00_setup_titanic_guia.pdf`
  - `01_Fundamentos_Datos_y_Control_Flujo.ipynb` y `01_fundamentos_guia.pdf`
  - `02_Funciones_y_POO_Cientifica.ipynb` y `02_poo_guia.pdf`
  - `03_Computacion_Vectorial_NumPy.ipynb` y `03_numpy_guia.pdf`
  - `04_Analisis_de_Datos_Pandas.ipynb` y `04_pandas_guia.pdf`
  - `05_Limpieza_y_Curacion_Datasets_CSIC.ipynb` y `05_limpieza_guia.pdf`
  - `06_Visualizacion_APIs_y_DigitalCSIC.ipynb` y `06_digital_csic_guia.pdf`
  - `07_Proyecto_Colaborativo_GitHub.ipynb`, `07_proyecto_github_guia.pdf` y `PROJECT_GUIDE.md`
- Ingesta de conceptos de los PDFs de transparencias (`FULL_COURSE_USE/PDFS/`) para crear guías PDF docentes side-by-side.
- Limpieza automatizada de scripts Python temporales de generación.

## [Desarrollo Minucioso Día 1 - Setup, Titanic, Fundamentos y Control de Flujo] - 2026-08-06

### Añadido
- Construcción exhaustiva paso a paso del **Día 1 (4 Horas)** en `NOTEBOOKS/WIP/`:
  - `00_Setup_y_Ejemplo_Inicial_Titanic.ipynb` y `00_setup_titanic_guia.pdf` (Bloque 1 - 2h): Ingesta de `CheckList_Instrucciones_Curso.md` del CSIC para setup de VSCode, venv e ipykernel + dataset del Titanic real de USE.
  - `01_Fundamentos_Datos_y_Control_Flujo.ipynb` y `01_fundamentos_guia.pdf` (Bloque 2 - 2h): Ingesta y fusión detallada de tipos primitivos, comentarios (`#`, docstrings), `f-strings` avanzadas, colecciones (`list`, `tuple`, `dict`, `set`), mutabilidad, rendimiento $\mathcal{O}(1)$ vs $\mathcal{O}(n)$, condicionales, bucles (`enumerate`, `zip`), list comprehensions y ejercicios prácticos con validación `assert`.

## [Módulo 05: Incorporación del Atributo Administrador (Clase Persona) en BibliotecaCientifica] - 2026-08-07

### Cambiado
- **Actualización de la Clase `BibliotecaCientifica` en [05_Intro_a_POO.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/WIP/DAY1/05_Intro_a_POO.ipynb):**
  - Añadido el parámetro y atributo `administrador=None` a la clase `BibliotecaCientifica`, restringido a objetos de tipo `Persona`.
  - Preservación íntegra de las ediciones del usuario en los docstrings y comentarios didácticos del cuaderno.
  - Actualización del método `resumen_repositorio()` para mostrar los metadatos completos del administrador/a responsable del repositorio (ejemplo: `Persona("Margarita", "Salas", "Centro de Biología Molecular Severo Ochoa (CSIC)")`).
  - Re-ejecución automatizada en `venv` y guardado del cuaderno **100% limpio (0 salidas retenidas)**.

## [Módulo 06: Creación del Cuaderno de Introducción a Pandas para Ciencia Abierta] - 2026-08-17

### Añadido
- **Creación y adaptación de [06_Intro_Pandas.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/06_Intro_Pandas.ipynb):**
  - Construcción del cuaderno del Módulo 06 a partir de `5_Intro_Pandas.ipynb` del curso CSIC, manteniendo el tono pedagógico de Gustavo Liñán Cembrano.
  - Implementación de la cabecera uniforme obligatoria (Celda 0) con imagen `![Logo Curso](../assets/LogoCurso_gemini.png)`, metadatos y objetivos de aprendizaje de Ciencia Abierta.
  - Explicación y ejercitación de importación (`import pandas as pd`), `Series`, `DataFrames`, indización explícita (`.loc`) y posicional (`.iloc`).
  - Carga e inspección de datasets reales con `vivienda.csv` (`read_csv`, `shape`, `head`, `tail`, `info`, `dtypes`).
  - Limpieza de datos: tratamiento de nulos (`dropna`, imputación con `fillna` mediante media/mediana/moda, `isnull().sum()`), conversión de fechas (`pd.to_datetime`, `.dt.year`), eliminación de duplicados (`duplicated`, `drop_duplicates`) y comparación de DataFrames (`equals`, `compare`).
  - Análisis de correlación (`.corr()`) entre variables numéricas.
  - Exportación a formatos abiertos y de publicación: LaTeX (`to_latex`), CSV (`to_csv`), Excel (`to_excel`), HTML (`to_html`) y JSON (`to_json`).
  - Incorporación de dependencias `openpyxl` y `jinja2` en `requirements.txt` e instalación en `./venv`.
  - Validación programática mediante `nbclient` en `./venv` con 0 errores y guardado 100% limpio de salidas de ejecución.

## [Módulo 07: Creación del Cuaderno de EDA y Curación de Metadatos de Digital.CSIC] - 2026-08-17

### Añadido
- **Creación y adaptación de [07_EDA_con_Pandas.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/07_EDA_con_Pandas.ipynb):**
  - Ingesta de 100 Handles aleatorios desde `DATASETS/FROM_DIGITALCSIC/input_handles.csv` mediante la librería `digital_csic` (`dcsic.fetch_records_batch`) aplicando 1s de cortesía de red entre peticiones OAI-PMH.
  - Inyección pedagógica de errores en celdas consecutivas: fechas multiplicadas por 10 (ej. `20210`), duplicación aleatoria de 5 registros, Handles malformados con sufijos alfabéticos y resúmenes nulos.
  - Flujo discursivo de EDA e inspección inicial (`shape`, `head`, `tail`, `info`, `describe`).
  - Pipeline de curación celda a celda: eliminación de duplicados por Handle (`drop_duplicates`), **validación de Handles mediante consulta directa de existencia al API/OAI-PMH de Digital.CSIC** (explicando pedagógicamente por qué la verificación real es superior a regex en producción), corrección de fechas fuera de rango (`year // 10`) e imputación de textos faltantes.
  - Análisis de producción científica por año y revistas más frecuentes.
  - Exportación del dataset curado final a `DATASETS/digital_csic_curated_100.csv`.
  - Instalación de la dependencia `lxml` en `./venv` y adición a `requirements.txt`.
  - Validación programática completa con `nbclient` en `./venv` obteniendo 0 errores y guardado 100% limpio de salidas.

## [Módulo 08: Visualización de Datos Científicos con Matplotlib y Pandas] - 2026-08-18

### Añadido
- **Creación y adaptación didáctica de [08_Intro_Matplotlib.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/08_Intro_Matplotlib.ipynb):**
  - Implementación de la cabecera uniforme obligatoria (Celda 0) con imagen `![Logo Curso](../assets/LogoCurso_gemini.png)`, metadatos y objetivos de aprendizaje de visualización científica.
  - Explicación de la arquitectura de Matplotlib: comparación didáctica entre la interfaz funcional (`pyplot`) y la interfaz orientada a objetos (`fig, ax = plt.subplots()`), destacando esta última como estándar para publicaciones de investigación.
  - Ejercitación de la tipología principal de gráficos: líneas (`plot`), barras verticales y horizontales (`bar`/`barh`), dispersión (`scatter` con escalas de color `cmap` y tamaño de punto) e histogramas/diagramas de caja (`hist`/`boxplot`).
  - Integración nativa con DataFrames de Pandas (`df.plot()`) conectando directamente con el dataset curado de `Digital.CSIC`.
  - Composición avanzada de subplots y paneles multi-figura mediante matrices `plt.subplots(2, 2)` y trazados asimétricos con `subplot2grid()`.
  - Exportación de gráficos con calidad de publicación científica: formatos de alta resolución (`PNG` a 300 DPI) y formatos vectoriales (`PDF`), aplicando ajuste de márgenes con `bbox_inches='tight'`.
  - Inclusión de ejercicios prácticos con autoevaluación y recursos de apoyo con Modelos de Lenguaje (IA).
  - Validación programática mediante `nbclient` en `./venv` con 0 errores y guardado 100% limpio de salidas de celda.

## [Módulo 09: Introducción a Google Colab y Computación en la Nube] - 2026-08-18

### Añadido
- **Creación y adaptación didáctica de [09_INTRO_GOOGLE_COLAB.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/09_INTRO_GOOGLE_COLAB.ipynb) y [09_Intro_Google_Colab.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/09_Intro_Google_Colab.ipynb):**
  - Implementación de la cabecera uniforme obligatoria (Celda 0) con imagen `![Logo Curso](../assets/LogoCurso_gemini.png)`, metadatos y objetivos de aprendizaje de computación en la nube.
  - Explicación detallada de la arquitectura de Google Colaboratory sobre máquinas virtuales Linux, aceleración gratuita con GPUs (NVIDIA T4/L4) y TPUs, trabajo colaborativo en tiempo real e integración con Gemini AI, Google Drive y GitHub.
  - Análisis de pros y contras (sesiones efímeras, desconexión por inactividad y políticas de confidencialidad de datos).
  - Tabla comparativa estructurada entre Google Colab (nube) y entornos locales de desarrollo (Antigravity-IDE / VS Code / Jupyter Local).
  - Configuración paso a paso de la API de Kaggle mediante tokens de autenticación (`kaggle.json`), permisos del sistema (`chmod 600`) y descarga programática de conjuntos de datos.
  - Ingesta y Análisis Exploratorio de Datos (EDA) sobre el dataset clínico de cáncer de tiroides (`Thyroid_Diff.csv`), incluyendo traducción de columnas, normalización de metadatos al español, simulación de inclusión de datos y exportación a `DATASETS/Thyroid_Diff_ES.csv`.
  - Visualización avanzada de patrones clínicos con Seaborn y Matplotlib: boxplots de edad por estadio tumoral, histogramas con KDE y diagramas de violín por categoría de riesgo.
  - Anexo interactivo de 15 minutos con formularios nativos `#@param` y controles dinámicos de `ipywidgets` (`@interact` y `@interact_manual`) anexados al final del cuaderno.
  - Validación programática mediante `nbclient` en `./venv` con 0 errores y guardado 100% limpio de salidas de ejecución.

## [Módulo 10: Acceso a Datos Repositoriales vía APIs y Protocolo OAI-PMH] - 2026-08-18

### Añadido
- **Creación y adaptación didáctica de [10_USANDO_API.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/10_USANDO_API.ipynb) y [10_Usando_API.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/10_Usando_API.ipynb):**
  - Implementación de la cabecera uniforme obligatoria (Celda 0) con imagen `![Logo Curso](../assets/LogoCurso_gemini.png)`, metadatos y objetivos de aprendizaje de APIs repositoriales.
  - Explicación comparativa estructurada entre arquitecturas de APIs RESTful modernas (JSON, endpoints por recurso, autenticación) y el protocolo internacional **OAI-PMH** (*Open Archives Initiative — Protocol for Metadata Harvesting*).
  - Análisis detallado del estándar de metadatos **Dublin Core** (`oai_dc`) y sus 15 elementos fundamentales (`dc:title`, `dc:creator`, `dc:date`, `dc:identifier`, etc.).
  - Peticiones HTTP reales al servidor de **Digital.CSIC** (`https://digital.csic.es/dspace-oai/request`) utilizando los verbos OAI-PMH `Identify` y `ListRecords`.
  - Parseo de respuestas XML con **BeautifulSoup** (`xml` parser) para la extracción de metadatos institucionales y el número total de publicaciones custodiadas mediante `resumptionToken` / `completeListSize`.
  - Búsqueda programática por palabras clave en títulos, extracción limpia de Handles (`10261/...`) y formateo de listas de autores con sus índices `[1], [2]`.
  - Conexión con la librería del curso (`lib/digital_csic.py`) demostrando la integración de funciones reutilizables (`dcsic.fetch_digital_csic_record`).
  - Inclusión de ejercicios prácticos con construcción de DataFrames de Pandas a partir del parseo de XML.
  - Validación programática mediante `nbclient` en `./venv` con 0 errores y guardado 100% limpio de salidas de celda.

## [Módulo 11: Modularización, Creación y Empaquetado de Librerías Reutilizables en Python] - 2026-08-19

### Añadido
- **Creación y adaptación didáctica de [11_Creacion_y_Empaquetado_de_Librerias_Python.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/11_Creacion_y_Empaquetado_de_Librerias_Python.ipynb) y [11_Empaquetado_de_Librerias_Python.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/11_Empaquetado_de_Librerias_Python.ipynb):**
  - Implementación de la cabecera uniforme obligatoria (Celda 0) con imagen `![Logo Curso](../assets/LogoCurso_gemini.png)`, metadatos oficiales del CSIC y objetivos pedagógicos (sin referencia a sesión).
  - Explicación accesible sobre por qué empaquetar código científico en Ciencia Abierta (reutilización sin copiar-pegar, reproducibilidad e integración con `pip`).
  - Guía práctica paso a paso de la estructura estandarizada `src/` recomendada por **pyOpenSci** mediante `copier` y `hatch`.
  - Análisis detallado del archivo `pyproject.toml` como corazón del empaquetado moderno (PEP 517 / PEP 621), especificando dependencias, autores y URLs.
  - Explicación del funcionamiento de la instalación en modo editable (`pip install -e .`) utilizando enlaces simbólicos para desarrollo interactivo continuo.
  - Ejemplificación modular con funciones matemáticas recursivas (`my_factorial`) y la clase de dominio `Persona` adaptada con listas estáticas de validación para institutos (IMSE, IMB, EBD, etc.) y servicios del CSIC (Biblioteca, Informática, Heladería, etc.).
  - Ejercicios prácticos con incorporación de nuevos centros del CSIC y validación de atributos mediante `@property` y setters.
  - Auditoría integral de importaciones en todos los cuadernos (`00` al `11`) y actualización de [requirements.txt](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/requirements.txt) estructurado por categorías (`requests`, `beautifulsoup4`, `scikit-learn`, `ipywidgets`, `pytest`, `copier`, `hatch`).
  - Validación programática mediante `nbclient` en `./venv` con 0 errores y guardado 100% limpio de salidas de celda.

## [Módulo 12: Control de Versiones en la Nube, Colaboración en GitHub y CI/CD con GitHub Actions] - 2026-08-19

### Añadido
- **Creación y adaptación didáctica de [12_INTRO_GITHUB.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/12_INTRO_GITHUB.ipynb):**
  - Implementación de la cabecera uniforme obligatoria (Celda 0) con imagen `![Logo Curso](../assets/LogoCurso_gemini.png)`, metadatos oficiales del CSIC y objetivos pedagógicos (sin referencia a sesión).
  - Explicación de la importancia de GitHub para la Ciencia Abierta, diferencias entre repositorios Públicos vs. Privados y protección de secretos (`.env`, credenciales) mediante `.gitignore`.
  - Guía didáctica para seleccionar licencias de software abierto (MIT, Apache 2.0, GPL).
  - Pasos guiados para crear repositorios remotos con el nombre del usuario (`<user_name>_PYTHON_CIENCIA_ABIERTA_2`) y vincular el paquete estandarizado local (`PYTHON_CIENCIA_ABIERTA_2`).
  - Explicación del flujo de trabajo con ramas (*Feature Branch Workflow*), comandos de Git (`git checkout -b`, `git commit`, `git push`) y creación de Pull Requests (PR) en la interfaz web de GitHub.
  - Introducción a la Integración Continua (CI/CD) analizando el flujo de automatización `.github/workflows/test.yml` proporcionado por pyOpenSci para ejecutar `pytest` automáticamente en la nube.
  - Ejercicios prácticos con verificación interactiva en Python del estado de seguridad del archivo `.gitignore`.
  - Validación programática mediante `nbclient` en `./venv` con 0 errores y guardado 100% limpio de salidas de celda.

## [Módulo 13: Introducción al Desarrollo de Software con Agentes en Antigravity-IDE] - 2026-08-20

### Añadido
- **Creación e implementación didáctica de [13_INTRO_DESARROLLO_AGENTES_ANTIGRAVITY.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/13_INTRO_DESARROLLO_AGENTES_ANTIGRAVITY.ipynb):**
  - Implementación de la cabecera uniforme obligatoria (Celda 0) con imagen `![Logo Curso](../assets/LogoCurso_gemini.png)`, metadatos oficiales del CSIC (Duración: 1 hora, Autor: Gustavo Liñán Cembrano, Módulo 13) y objetivos pedagógicos.
  - Explicación comparativa del salto cualitativo entre el autocompletado pasivo en línea (*Ghost Text* `Tab`), la refactorización asistida (`Cmd+K`) y la **Programación Basada en Agentes Autónomos** en Antigravity-IDE.
  - Fundamentación teórica y formalización matemática en $\LaTeX$ del bucle cerrado **Percepción - Acción - Verificación (PAV)**.
  - Creación paso a paso de la arquitectura de agentes en la raíz del espacio de trabajo:
    - **Reglas (`.agents/rules/curacion_abierta.md`):** Directivas éticas y técnicas de curación.
    - **Habilidades (`.agents/skills/open-science-curator/SKILL.md`):** Protocolo de actuación con cabecera YAML.
    - **Herramientas (`Tools`):** Funciones Python con consultas HTTP REALES al servidor OAI-PMH de **Digital.CSIC** (`https://digital.csic.es/dspace-oai/request`) usando `requests` y `BeautifulSoup`.
  - Integración del SDK oficial de **Google Gemini (`google-genai`)** con **Function Calling / Tool Calling**:
    - Carga dinámica del System Instruction unificando reglas y habilidades de `.agents/`.
    - Envío del esquema de herramientas a Gemini (`gemini-2.5-flash`).
    - Gestión defensiva de secretos con `python-dotenv` y detección enmascarada de `GEMINI_API_KEY`.
    - Mecanismo de respaldo automático (*Fallback*) a `DIRECT_TOOL_ORCHESTRATION` ante límites de cuotas (`429 RESOURCE_EXHAUSTED`) garantizando 0 fallos de ejecución.
  - Refactorización orientada a objetos incorporando el método `agent.generate_summary_report()` y procesamiento por lotes con retraso cortés (`time.sleep(1)`) e integración con `lib.mylib.linea`.
  - Validación programática mediante `nbclient` en `./venv` con 0 errores y guardado 100% limpio de salidas de celda.

## [Módulo 14: Proyecto Final Integrador en GitHub] - 2026-08-21

### Añadido
- **Creación e implementación didáctica de [14_PROYECTO_FINAL_GITHUB.ipynb](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/NOTEBOOKS/14_PROYECTO_FINAL_GITHUB.ipynb):**
  - Implementación de la cabecera uniforme obligatoria (Celda 0) con la imagen `![Logo Curso](../assets/LogoCurso_gemini.png)`, metadatos oficiales del CSIC (Duración: 2 horas, Autor: Gustavo Liñán Cembrano, Módulo 14) y objetivos pedagógicos.
  - Diseño de la práctica integradora colaborativa basada en el proyecto `CSIC-ClimateWatch` ([https://github.com/guslicem/proyecto_final_curso_python_2026](https://github.com/guslicem/proyecto_final_curso_python_2026)) con 13.056 observaciones climáticas mensuales reales (1961 - 2024).
  - Plan de Acción por Equipos (~45 min):
    - **Equipo 1 (Backend):** Función `get_hottest_and_coldest_year(df, start_year, end_year, comunidades)`.
    - **Equipo 2 (Frontend):** Visualización de días en ola de calor, alerta dinámica si $> 20$ y comparativa vs media nacional en Streamlit (`app.py`).
    - **Equipo 3 (Docs FAIR):** Glosario de columnas en `README.md`, archivo `CITATION.cff` y edición activa de `CHANGELOG.md` durante la revisión de PRs.
    - **Equipo 4 (Testing & CI):** Ampliación de `tests/test_metrics.py` y creación de `tests/test_data_loader.py`.
  - Guía detallada del flujo Git/GitHub (Fork, Clone, rama `feature/`, Commit, Push, Pull Request y *Peer Review*).
  - Protocolo de integración y publicación de la **Release v1.0.0** en GitHub por parte del profesor.
  - Arreglo de pruebas unitarias en `PROYECTO_FINAL/tests/test_data_loader.py` con **7/7 PASADAS ✅**.
  - Validación programática mediante `nbclient` en `./venv` con 0 errores y guardado 100% limpio de salidas de celda.

## [Directorio Documentación y Exportación PDF] - 2026-08-21

### Añadido
- **Incorporación del directorio `doc/`:** Estructura oficial `doc/PDFS/NOTEBOOKS/` y `doc/DOC_DE_INTERES/` para organizar la documentación de referencia y exportaciones impresas.
- **Herramienta de automatización [`utils/export_notebooks_to_pdf.py`](file:///Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2/utils/export_notebooks_to_pdf.py):** Script en Python para escanear `NOTEBOOKS/` y generar automáticamente los PDFs vectorizados de los 15 cuadernos del curso (15/15 generados con éxito).
- **Gestión de Exclusiones en `.gitignore`:** Exclusión explícita de `utils/` y `scratch/` para mantener limpio el repositorio remoto de GitHub.

## [Documentación - Presentaciones PDF en doc/PDFS/SLIDES/] - 2026-08-24

### Añadido
- Actualización del archivo `README.md` documentando la existencia del directorio `doc/PDFS/SLIDES/` con las presentaciones teóricas del curso en formato PDF (`Modulo_1_Introduccion.pdf`, `Modulo_2_Fundamentos_de_python.pdf`).

## [Git - Exclusión de Skills Locales en .gitignore] - 2026-08-24

### Cambiado
- Exclusión de los directorios `.agents/skills/ai-coding-assistant-module/` y `.agents/skills/course_learner/` en `.gitignore`.
- Eliminación de la copia remota de estos skills en el seguimiento de Git para mantenerlos exclusivamente en local.







