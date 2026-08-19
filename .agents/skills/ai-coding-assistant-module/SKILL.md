---
name: ai-coding-assistant-module
description: Diseña e implementa módulos de código Python (.py), manuales de documentación PDF y arneses de pruebas en Jupyter para enseñar asistentes de IA, autocompletado contextual y depuración interactiva en Antigravity-IDE.
---

# Skill: Módulo de Asistentes de Código con IA, Depuración y Programación Basada en Agentes

## Propósito
Guiar la creación de contenidos docentes centrados en enseñar el uso de asistentes de codificación con IA, autocompletado inteligente contextual (*Ghost Text* en gris), refactorización asistida (`Cmd+K`) y desarrollo orientado a agentes autónomos en Antigravity-IDE.

Ante la limitación del autocompletado por IA dentro del editor de celdas de cuadernos Jupyter, este módulo adopta un **Flujo Dual Integrado**:
- **Desarrollo de Código:** Archivos de módulo Python (`.py`) ejecutables, donde el autocompletado en línea (`Tab` / `Cmd+→`), la refactorización (`Cmd+K`) y la depuración interactiva paso a paso (`F5`, breakpoints) funcionan al 100%.
- **Documentación Paralela:** Manuales en formato **PDF** generados automáticamente e inspeccionables side-by-side en el IDE.
- **Evaluación y Arnés de Pruebas:** Cuadernos Jupyter (`.ipynb`) que importan las funciones del módulo `.py`, ejecutan tests de validación (`assert`) y ofrecen representaciones gráficas e interactivas.

---

## Directivas de Ejecución

### 1. Encabezado Visual y Ruta del Logo
- La carpeta de imágenes `assets/` se encuentra **siempre situada en la raíz del repositorio**.
- En la celda Markdown inicial de cada cuaderno Jupyter, se debe incluir la imagen del logo del curso calculando la ruta relativa exacta según la profundidad del cuaderno respecto a la raíz:
  - Para cuadernos en `NOTEBOOKS/WIP/`: `![Logo Curso](../../assets/LogoCurso_gemini.png)`
  - Para cuadernos en `NOTEBOOKS/`: `![Logo Curso](../assets/LogoCurso_gemini.png)`

### 2. Entorno de Trabajo en Pantalla Dividida (Dual-Pane IDE Workflow)
- **Panel Izquierdo:** Archivo ejecutable `.py` (donde el alumnado completa las funciones con la asistencia de IA y depura el código usando puntos de interrupción y el depurador nativo de VS Code / Antigravity-IDE).
- **Panel Derecho:** Manual de teoría/enunciados en formato **PDF** (o cuaderno complementario `.ipynb`) abierto como referencia al lado del código.

### 3. Generación de Documentación en PDF y Limpieza Automatizada
- Cada módulo debe compilar su guía docente en PDF utilizando scripts auxiliares en Python basados en la librería `fpdf2` instalada en el entorno virtual (`./venv/bin/python`).
- **Limpieza de Archivos Auxiliares (REGLA OBLIGATORIA):** Al finalizar la generación y compilación exitosa de las guías PDF y cuadernos `.ipynb`, el agente **DEBE eliminar automáticamente todos los archivos Python auxiliares y temporales** (tales como `crear_*.py`, `generar_*.py`, `test.py` o scripts de prueba), asegurando que en `NOTEBOOKS/` o `NOTEBOOKS/WIP/` permanezcan **únicamente los archivos finales del curso (`.py`, `.pdf`, `.ipynb`)**.

### 4. Estructura Didáctica por Módulo

#### Módulo 15: Autocompletado Inteligente, Refactorización y Depuración Interactiva
- **Módulo Python (`15_asistencia_ia_modulo.py`):** Contiene plantillas de funciones con anotaciones de tipos, docstrings, bloques `# TODO` para autocompletado por IA, y funciones preparadas para depuración paso a paso con puntos de interrupción (`F5`).
- **Documento PDF (`15_asistencia_ia_guia.pdf`):** Contiene los objetivos CSIC, teoría del autocompletado por IA (*Context-awareness*, *Ghost Text* en gris, atajos `Tab`, `Cmd+→`, `Cmd+K`), guía de uso del depurador nativo (`F5`, inspección de variables, pila de llamadas) y soporte LaTeX ($\LaTeX$).
- **Cuaderno Arnés (`15_Autocompletado_y_Depuracion_IA.ipynb`):** Importa las funciones del módulo `.py` completadas por el alumno, ejecuta tests unitarios interactivos con `assert` y genera gráficos bibliométricos (`matplotlib` / `pandas`).

#### Módulo 16: Programación Basada en Agentes Autónomos (Agentic Coding)
- **Módulo Python (`16_agentes_autonomos_modulo.py`):** Implementación de la clase `ScientificAgent` bajo el ciclo **Percepción-Acción-Verificación**, definición de herramientas (*Tool-Calling*) para repositorios científicos (Digital.CSIC) y formateo BibTeX.
- **Documento PDF (`16_agentes_autonomos_guia.pdf`):** Fundamentación del paradigma de agentes, ciclo de Percepción-Acción-Verificación, diagramas de flujo y rastreo de trazabilidad (*history / logs*).
- **Cuaderno Arnés (`16_Programacion_Basada_en_Agentes_Antigravity.ipynb`):** Arnés de evaluación interactiva para orquestar agentes, inspeccionar logs de ejecución y validar respuestas con aserciones.

---

## Trazabilidad y Sincronización Obligatoria
1. Actualizar la matriz conceptual y mapa de fuentes en `artifacts/source_index.md`.
2. Registrar detalladamente los cambios en `artifacts/changelog.md` y replicar la misma entrada de forma exacta en `CHANGELOG.md` y `README.md`.
