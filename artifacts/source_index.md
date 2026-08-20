# Mapa Conceptual e Índice de Fuentes Unificado: Python para Ciencia Abierta (20 Horas / CSIC)

## 1. Resumen Ejecutivo y Auditoría de Materiales

Este documento constituye la indización conceptual, auditoría de redundancias y plan de unificación para el curso de **20 Horas (5 Días x 4 Horas)** de **Python para Ciencia Abierta**, diseñado específicamente para el personal investigador y técnico del **CSIC**.

El mapa conceptual ha sido generado tras el análisis exhaustivo y la fusión avanzada de los dos repositorios docentes de origen:
- **`FULL_COURSE_USE/` (Universidad de Sevilla):** Iteración pedagógica de fundamentos de programación. Aporta la frescura pedagógica en conceptos básicos (`0` a `4`), **Programación Orientada a Objetos (`5_Intro_a_POO.ipynb`)**, **NumPy (`6_Intro_a_Numpy.ipynb`)** y el banco de transparencias en `FULL_COURSE_USE/PDFS/`.
- **`FULL_COURSE_CSIC/` (Consejo Superior de Investigaciones Científicas):** Especialización en **Ciencia Abierta, Datos y Automatización**. Destaca en **Pandas**, **Matplotlib/Seaborn**, **Git/GitHub**, **APIs REST**, **Handles y Metadatos de Digital.CSIC**, y despliegue colaborativo.

---

## 2. Matriz de Fusión Didáctica y Distribución en 20 Horas (5 Días)

| Jornada / Módulo | Contenido en `FULL_COURSE_USE` | Contenido en `FULL_COURSE_CSIC` | Decisión y Plan de Elevación Técnica |
|---|---|---|---|
| **Día 1: Setup y Fundamentos (4h)** | `0_Ejemplo_TITANIC`, `1_Intro_Tipos_Datos`, `2_Estructuras`, `4_Control` | `SESION0/` (Setup VSCode, venv) + `MODULO2/` | **Fusión Elevada:** Setup riguroso del CSIC + Titanic de USE + Tipos de datos, colecciones y estructuras de control con tipado estático (`typing`). |
| **Día 2: POO y NumPy (4h)** | `3_Scripts_Y_Funciones`, `5_Intro_a_POO`, `6_Intro_a_Numpy` | `MODULO2/` + `MYLIBS/utils.py` | **Fusión Elevada:** Funciones con `*args`/`**kwargs`, diseño de clases (`class`) y computación vectorial con NumPy. |
| **Día 3: Pandas, Corrupción y Limpieza (4h)** | No presente | `MODULO3/5_Intro_Pandas`, `6_EDA_Pandas` | **Especialización CSIC + Inserción de Corrupción:** DataFrames, filtrado, `groupby`, simulación de datos dañados y técnicas avanzadas de curación. |
| **Día 4: Visualización, APIs, Digital.CSIC e IA (4h)** | Mención en slides | `MODULO4/11_web_scraping`, `12_using_api`, `14_metadata` | **Integración de Ingesta por Handles + Skill IA:** Visualización con Matplotlib/Seaborn, resolución por Handles de **Digital.CSIC** + Flujo Dual (Módulos `.py`, PDF side-by-side, arnés `.ipynb` y agentes autónomos). |
| **Día 5: Proyecto Colaborativo en GitHub (4h)** | Mención en slides | `MODULO4/10_Intro_GitHub` | **Proyecto Integrador en Equipos:** Trabajo en ramas (`feature/`), commits, Pull Requests, revisiones asistidas por IA y resolución de conflictos de fusión. |

---

## 3. Secuencia Didáctica de Cuadernos y Guías PDF (`NOTEBOOKS/WIP/DAYX/`)

```
NOTEBOOKS/WIP/
├── DAY1/
│   ├── 00_guia_instalacion_antigravity_ide.pdf      [Día 1 - Guía de Instalación Antigravity-IDE]
│   ├── 00_Setup_y_Ejemplo_Inicial_Titanic.ipynb     [Día 1 - Bloque 1 Notebook]
│   ├── 01_Intro_Tipos_Datos.ipynb                    [Día 1 - Bloque 2.1 Notebook]
│   ├── 02_Estructuras_de_Datos.ipynb                 [Día 1 - Bloque 2.2 Notebook]
│   ├── 03_Control_de_Flujo.ipynb                     [Día 1 - Bloque 2.3 Notebook]
│   ├── 01_dia1_fundamentos_guia.pdf                  [Día 1 - Guía Docente PDF]
│   └── _build_day1.py                                [Script de Construcción Día 1]
├── DAY2/
│   ├── 04_Funciones_Avanzadas.ipynb                  [Día 2 - Bloque 1 Notebook]
│   ├── 05_POO_Cientifica_Desde_Cero.ipynb            [Día 2 - Bloque 2 Notebook]
│   └── 06_Computacion_Vectorial_NumPy.ipynb         [Día 2 - Bloque 3 Notebook]
├── DAY3/
│   ├── 07_Analisis_de_Datos_Pandas.ipynb             [Día 3 - Bloque 1 Notebook]
│   └── 08_Limpieza_y_Curacion_Datasets_CSIC.ipynb    [Día 3 - Bloque 2 Notebook]
├── DAY4/
│   ├── 09_Visualizacion_APIs_y_DigitalCSIC.ipynb     [Día 4 - Bloque 1 Notebook]
│   ├── 15_asistencia_ia_modulo.py                    [Día 4 - Módulo Asistencia IA]
│   ├── 12_INTRO_GITHUB.ipynb                         [Control de Versiones y CI/CD]
│   └── 13_INTRO_DESARROLLO_AGENTES_ANTIGRAVITY.ipynb [Desarrollo Asistido por Agentes IA]
└── DAY5/
    ├── 10_Proyecto_Colaborativo_GitHub.ipynb         [Día 5 - Notebook de Proyecto]
    └── PROJECT_GUIDE.md                              [Día 5 - Guía de Trabajo en Equipos]
```

---

## 4. Metodología de Corrupción y Curación de Datos de Digital.CSIC

Para capacitar al personal investigador en la gestión de metadatos imperfectos en escenarios reales:
1. **Obtención por Handles:** Ingesta directa de registros de publicaciones mediante la resolución de sus Handles oficiales de Digital.CSIC (`http://hdl.handle.net/10261/...`).
2. **Inyección de Ruido Simulado:**
   - Inconsistencia en DOIs (`10.1038/...`, `doi:10.1038/...`, `http://dx.doi.org/...`).
   - Heterogeneidad en fechas (`2024-05-10`, `10/05/2023`, `2022`).
   - Nombres de autores no estandarizados (`GARCIA, ALBERTO `, `Martínez, L.; Sánchez, P.`).
   - Espacios redundantes y nulos implícitos.
3. **Curación Programática con Pandas e IA:**
   - Construcción de canalizaciones (*pipelines*) de limpieza en Pandas.
   - Uso de expresiones regulares (`re`) y sugerencia en línea por IA (*Ghost Text* y `Cmd+K`).
   - Validación mediante aserciones (`assert`).

---

## 5. Dinámica del Día 5: Proyecto Integrador Colaborativo en Equipos

- **Equipos Multidisciplinares:** 3 a 4 personas por equipo.
- **Workflow de Git/GitHub:**
  - Repositorio público creado por el Maintainer del equipo.
  - Protección de rama `main` y desarrollo en ramas temáticas (`feature/ingesta`, `feature/limpieza`, `feature/analisis`, `feature/agente`).
  - Creación de Pull Requests (PR) obligatorios con *Peer Code Review* asistido por IA.
  - Simulación y resolución guiada de *Merge Conflicts*.
