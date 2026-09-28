# Regla de Dominio: Auditoría de Calidad y Viabilidad Docente del Curso

## Directivas Principales de Auditoría:

1. **Auditoría de Correctitud de Contenidos y Código:**
   - Verificar la coherencia conceptual de los cuadernos de Jupyter en `NOTEBOOKS/` (Módulos 00 al 14).
   - Validar sintaxis de código en Python 3.10+, convenciones PEP 8, ausencia de dependencias no declaradas en `requirements.txt` y robustez de funciones auxiliares en `lib/`.
   - Garantizar el principio defensivo en llamadas HTTP a servicios externos (APIs, OAI-PMH Digital.CSIC, Google Colab, Kaggle, GitHub).

2. **Verificación de Enlaces e Hipervínculos:**
   - Comprobar la sintaxis y vigencia de todos los enlaces externos (Google Forms de autoevaluación, URLs de Handles `10261/XXX`, DOIs `10.XXX/YYY`, repositorios GitHub).
   - Detectar posibles enlaces rotos o URLs no relativas que impidan la portabilidad entre plataformas.

3. **Auditoría de Calidad Gráfica y Visual:**
   - Verificar la presencia obligatoria de la cabecera del curso y el logo oficial (`![Logo Curso](../assets/LogoCurso_gemini.png)`) en la Celda 0 de todos los cuadernos.
   - Comprobar la calidad y formato de gráficos científicos (Matplotlib/Seaborn): resolución mínima 300 DPI, presencia de etiquetas en ejes (`xlabel`, `ylabel`), leyendas descriptivas y paletas de color accesibles.
   - Confirmar que las compilaciones PDF en `doc/PDFS/NOTEBOOKS_PDFs/` incrusten adecuadamente los gráficos y mantengan la legibilidad tipográfica.

4. **Verificación de Viabilidad Horaria (20 Horas Lectivas / 4 Sesiones de 5 Horas):**
   - Auditar que la carga docente total de los 15 cuadernos interactivos sea viable para ser impartida en **4 jornadas intensivas de 5 horas (20 horas totales)** para personal investigador y técnico del CSIC.
   - Verificar la distribución temporal por sesión:
     - **Sesión 1 (5h - Módulos 00 a 03):** Setup, Antigravity-IDE, Tipos Primitivos, Estructuras de Datos, Scripts y Funciones.
     - **Sesión 2 (5h - Módulos 04 a 06):** Control de Flujo, Manejo de Excepciones, POO e Introducción a Pandas.
     - **Sesión 3 (5h - Módulos 07 a 10):** EDA con Digital.CSIC, Visualización con Matplotlib/Seaborn, Google Colab y APIs OAI-PMH.
     - **Sesión 4 (5h - Módulos 11 a 14):** Empaquetado pyOpenSci, GitHub & CI/CD Actions, Desarrollo Asistido por Agentes IA y Proyecto Final Integrador.
5. **Protocolo Estricto de Exportación a PDF de Informes:**
   - La exportación a PDF de los informes de auditoría debe realizarse mediante la plantilla HTML estilizada y el motor de impresión Chrome Headless.
   - Aplicar reglas CSS de ancho fijo (`table-layout: fixed`, `word-wrap: break-word`) y porcentajes explícitos en columnas de tablas para evitar recortes laterales en páginas A4.
   - Representar la temporización mediante barras visuales HTML/CSS nativas para evitar bloques de código CSS desbordados procedentes de Mermaid.
   - Forzar el salto de página (`page-break-before: always`) antes del Análisis DAFO para garantizar una página especializada de 1 hoja limpia.
