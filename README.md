# Python para Ciencia Abierta (CSIC) — Edición 2026

![Licencia MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-green.svg)
![IDE](https://img.shields.io/badge/IDE-Antigravity--IDE-orange.svg)

Bienvenid@ al repositorio oficial del curso **Python para Ciencia Abierta**, diseñado e impartido específicamente para el personal investigador, técnico y de apoyo a la investigación del **Consejo Superior de Investigaciones Científicas (CSIC)**.

---

## 👨‍🏫 Información del Curso e Impartición

- **Denominación del Curso:** Iniciación a Python para Ciencia Abierta (Edición CSIC)
- **Fechas Oficiales:** 5 a 8 de Octubre de 2026, Aula SGAI, C/Pinar 19, Madrid.
- **Profesor y Autor:** Gustavo Liñán Cembrano  
- **Afiliación:** Instituto de Microelectrónica de Sevilla (IMSE-CNM / CSIC-Universidad de Sevilla)
- **Correo de Contacto:** `gustavo.linan@csic.es` | `guslicem@us.es`

---

## 🎯 Descripción y Objetivos

Este curso proporciona una formación sólida e interactiva desde cero en el lenguaje de programación **Python**, orientada al tratamiento de datos científicos, la reproducibilidad y las prácticas de **Ciencia Abierta**.

A lo largo del temario se cubren los siguientes bloques docentes:

1. **Entorno de Trabajo Científico:** Configuración de entornos virtuales (`venv`), Jupyter Notebooks y asistencia inteligente con **Antigravity-IDE**.
2. **Tipos Primitivos y Colecciones:** Cadenas de texto, números, listas, tuplas, conjuntos (`set`) y diccionarios (`dict`).
3. **Scripts, Modularización y Funciones:** Funciones (`def`), expresiones `lambda`, documentación con docstrings y módulos reutilizables (`lib/`).
4. **Control de Flujo y Manejo de Excepciones:** Condicionales, bucles (`for`, `while`, `enumerate`, `zip`) y gestión defensiva de errores (`try-except`).
5. **Introducción a la POO:** Clases, objetos, herencia, métodos dunder y modelado de entidades científicas (`Persona`, `Registro`).
6. **Ciencia de Datos y Análisis Exploratorio (EDA):** Manipulación de metadatos y datasets masivos con **Pandas** y **NumPy**.
7. **Curación de Datos Científicos y OAI-PMH:** Descarga programática de repositorios abiertos (**Digital.CSIC**), verificación de Handles e imputación de nulos.
8. **Visualización de Datos Científicos:** Gráficos estáticos y vectoriales de calidad de publicación con **Matplotlib** y **Seaborn**.
9. **Computación en la Nube e Interactividad:** Uso de **Google Colab**, aceleración por GPU/TPU, integración con la API de **Kaggle** y formularios/widgets interactivos (`ipywidgets` / `#@param`).

---

## 📚 Estructura de Cuadernos (`NOTEBOOKS/`)

Todos los cuadernos han sido validados programáticamente y se encuentran guardados 100% limpios de salidas para la realización de los ejercicios:

- **`00_Setup_y_Ejemplo_Inicial_Titanic.ipynb`**: Demostración inicial de análisis de datos con el dataset Titanic.
- **`01_Intro_Tipos_Datos.ipynb`**: Variables, tipos primitivos, mutabilidad y conversión de tipos.
- **`02_Estructuras_de_Datos.ipynb`**: Colecciones avanzadas (listas, tuplas, diccionarios y conjuntos).
- **`03_Scripts_y_Funciones.ipynb`**: Creación de scripts `.py`, paso de parámetros, retorno de tuplas y modularidad.
- **`04_Control_de_Flujo.ipynb`**: Estructuras de control, iteradores y captura de excepciones.
- **`05_Intro_a_POO.ipynb`**: Programación Orientada a Objetos aplicada a investigación.
- **`06_Intro_Pandas.ipynb`**: Ingesta de datos, filtrado, estadísticas y exportación a formatos abiertos (LaTeX, CSV, Excel, HTML, JSON).
- **`07_EDA_con_Pandas.ipynb`**: Exploración y curación de metadatos reales descargados de **Digital.CSIC** vía OAI-PMH.
- **`08_Intro_Matplotlib.ipynb`**: Arquitectura orientada a objetos (`fig, ax`), composición de subplots y exportación a alta resolución (PNG 300 DPI / PDF).
- **`09_INTRO_GOOGLE_COLAB.ipynb`**: Computación en la nube con Colab, API de Kaggle, GPUs/TPUs, EDA biomédico y anexo de **Widgets interactivos** (`ipywidgets` / `#@param`).
- **`10_USANDO_API.ipynb`**: Acceso a datos repositoriales en **Digital.CSIC** mediante el protocolo **OAI-PMH**, parseo de respuestas XML con BeautifulSoup, extracción de esquema Dublin Core (`oai_dc`) e integración con `lib/digital_csic.py`.
- **`11_CREACION_Y_EMPAQUETADO_LIBRERIAS.ipynb`**: Modularización, creación y empaquetado de librerías reusables en Python, estándar `src/`, `pyproject.toml`, mejores prácticas de **pyOpenSci** e instalación en modo editable (`pip install -e .`).
- **`12_INTRO_GITHUB.ipynb`**: Control de versiones en la nube con GitHub, repositorios `<user_name>_PYTHON_CIENCIA_ABIERTA_2`, privacidad/licencias, *Feature Branch Workflow*, Pull Requests y **CI/CD con GitHub Actions** (`pytest` en la nube).
- **`13_INTRO_DESARROLLO_AGENTES_ANTIGRAVITY.ipynb`**: Paradigma de desarrollo asistido por Agentes IA en **Antigravity-IDE**, bucle Percepción-Acción-Verificación (PAV), directivas del proyecto (`AGENTS.md`), habilidades (`Skills`) y creación de `OpenScienceAgent` en Python con integración del SDK oficial de **Gemini (`google-genai`)**, **Function Calling / Tool Calling**, peticiones OAI-PMH en vivo a **Digital.CSIC**, gestión defensiva de claves (`.env`) y mecanismo de respaldo automático (*fallback*) ante límites de cuota.

---

## 🚀 Entorno Recomendado: Antigravity-IDE

Este curso ha sido optimizado y configurado para ser ejecutado con **Antigravity-IDE**, el entorno de desarrollo nativo asistido por IA.

### 📥 Enlace de Descarga Oficial
Puedes descargar gratis la versión oficial de **Antigravity-IDE** desde:  
👉 **[Descargar Antigravity-IDE](https://antigravity.google)**

---

## 🛠️ Guía Rápida de Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/guslicem/PYTHON_PARA_CIENCIA_ABIERTA_2.git
cd PYTHON_PARA_CIENCIA_ABIERTA_2
```

### 2. Crear y Activar el Entorno Virtual de Python
```bash
# Crear el entorno virtual en la carpeta venv
python3 -m venv venv

# Activar el entorno virtual en macOS / Linux:
source venv/bin/activate

# Activar el entorno virtual en Windows:
venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Extensiones Recomendadas en Antigravity-IDE / VS Code
- **Python (`ms-python.python`):** Soporte oficial para lenguaje Python y `venv`.
- **Pylance (`ms-python.vscode-pylance`):** Autocompletado e inspección estática de tipos.
- **Jupyter (`ms-toolsai.jupyter`):** Visualización y ejecución interactiva de cuadernos `.ipynb`.
- **Rainbow CSV (`mechatroner.rainbow-csv`):** Coloreado sintáctico de archivos `.csv`.

---

## 📁 Estructura del Proyecto

- **`NOTEBOOKS/`**: Cuadernos del curso en formato Jupyter Notebook (`.ipynb`).
- **`DATASETS/`**: Conjuntos de datos reales (`.csv`, `.xlsx`, `.pdf`) para ejercicios prácticos (`digital_csic_curated.csv`, `Thyroid_Diff_ES.csv`, `vivienda.csv`, etc.).
- **`lib/`**: Librería personalizada del curso con utilidades de descarga OAI-PMH (`digital_csic.py`) y formato (`mylib.py`).
- **`artifacts/`**: Documentación técnica del repositorio y changelog histórico (`artifacts/changelog.md`).
- **`CHANGELOG.md`**: Registro cronológico de cambios y versiones del curso.

---

## 📜 Licencia

Este proyecto y todos sus materiales docentes están distribuidos bajo la **Licencia MIT**. Consulta el archivo [`LICENSE`](LICENSE) para más detalles.
