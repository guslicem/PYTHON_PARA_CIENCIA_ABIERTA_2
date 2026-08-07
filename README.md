# Python para Ciencia Abierta (CSIC) — Edición 2026

![Licencia MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-green.svg)
![IDE](https://img.shields.io/badge/IDE-Antigravity--IDE-orange.svg)

Bienvenid@ al repositorio oficial del curso **Python para Ciencia Abierta**, diseñado e impartido específicamente para el personal investigador, técnico y personal de apoyo a la investigación del **Consejo Superior de Investigaciones Científicas (CSIC)**.

---

## 👨‍🏫 Información del Curso e Impartición

- **Denominación del Curso:** Iniciación a Python para Ciencia Abierta (Edición CSIC)
- **Fechas Oficiales:** 5 a 8 de Octubre de 2026
- **Profesor y Autor:** Gustavo Liñán Cembrano  
- **Afiliación:** Instituto de Microelectrónica de Sevilla (IMSE-CNM / CSIC-Universidad de Sevilla)
- **Correo de Contacto:** `glinan@us.es` | `linan@imse-cnm.csic.es`

---

## 🎯 Descripción y Objetivos

Este curso proporciona una formación sólida e interactiva desde cero en el lenguaje de programación **Python**, orientada específicamente al tratamiento de datos científicos, reproducibilidad y prácticas de **Ciencia Abierta**.

A lo largo del temario se cubren los siguientes bloques:
1. **Entorno de Trabajo Científico:** Configuración de entornos virtuales (`venv`), Jupyter Notebooks y asistencia inteligente por IA.
2. **Tipos Primitivos y Colecciones:** Cadenas de texto, listas, tuplas, conjuntos (`set`) y diccionarios (`dict`).
3. **Scripts, Modularización y Funciones:** Funciones, bibliotecas personalizadas e ingesta de argumentos.
4. **Control de Flujo y Manejo de Excepciones:** Condicionales, bucles (`for`, `while`, `enumerate`, `zip`) y gestión defensiva de errores (`try-except`).
5. **Introducción a la POO:** Clases, objetos, composición y funciones hash para el modelado de repositorios científicos.
6. **Ciencia de Datos y Análisis Exploratorio:** Manipulación de conjuntos de datos masivos con **Pandas**, matrices con **NumPy** y visualización de datos con **Matplotlib / Seaborn**.

---

## 🚀 Entorno Recomendado: Antigravity-IDE

Este curso ha sido optimizado y configurado para ser ejecutado con **Antigravity-IDE**, el entorno de desarrollo nativo asistido por Inteligencia Artificial de Google.

### 📥 Enlace de Descarga Oficial
Puedes descargar gratis la versión oficial de **Antigravity-IDE** desde el siguiente enlace oficial:  
👉 **[Descargar Antigravity-IDE](https://antigravity.google)**

---

## 🛠️ Guía Rápida de Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/PythonParaCienciaAbierta_2.git
cd PythonParaCienciaAbierta_2
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
Para disfrutar de la mejor experiencia docente y autocompletado inteligente, instala las siguientes extensiones en tu IDE:

- **Python (`ms-python.python`):** Soporte nativo para Python y gestión de `venv`.
- **Pylance (`ms-python.vscode-pylance`):** Autocompletado rápido e inspección estática de tipos.
- **Jupyter (`ms-toolsai.jupyter`):** Edición y ejecución interactiva de cuadernos `.ipynb`.
- **Rainbow CSV (`mechatroner.rainbow-csv`):** Coloreado sintáctico de datasets `.csv`.

---

## 📁 Estructura del Repositorio

- **`NOTEBOOKS/`**: Contiene las lecciones del curso organizadas en cuadernos interactivos de Jupyter (`.ipynb`) listos y limpios para la realización de ejercicios.
- **`DATASETS/`**: Archivos de datos reales (`.csv`, `.xlsx`, `.json`) utilizados en las prácticas de investigación y análisis exploratorio (EDA).
- **`requirements.txt`**: Lista completa de librerías y dependencias en Python necesarias para el seguimiento del curso.

---

## 📜 Licencia

Este proyecto y todos sus materiales docentes están distribuidos bajo la **Licencia MIT**. Consulta el archivo [`LICENSE`](LICENSE) para más detalles.
