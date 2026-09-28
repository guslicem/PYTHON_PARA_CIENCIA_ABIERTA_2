---
name: course-content-auditor
description: Protocolo de auditoría estática de código Python, validación sintáctica de celdas de cuadernos Jupyter, detección de dependencias y verificación de enlaces HTTP/Handles de Digital.CSIC.
---

# Skill: Auditor de Código, Enlaces y Contenido Técnico

## Objetivos del Skill:
Esta habilidad proporciona el protocolo analítico para auditar la calidad sintáctica, técnica y la integridad de los cuadernos docentes (`NOTEBOOKS/*.ipynb`).

## Protocolo de Actuación:

1. **Inspección Sintáctica de Celdas:**
   - Parsear el árbol JSON de cada cuaderno (`nbformat.read`).
   - Extraer celdas de código (`cell_type == "code"`) y verificar sintaxis de Python 3.10+ mediante `ast.parse`.
   - Comprobar que no existan variables no inicializadas ni dependencias no instalables.

2. **Auditoría de Enlaces e Hipervínculos:**
   - Escanear todas las celdas Markdown en busca de URLs con expresiones regulares (`https?://[^\s)]+`).
   - Clasificar enlaces en:
     - **Formularios de Autoevaluación:** Cuestionarios de Google Forms.
     - **Handles Institucionales:** Resolutores de Digital.CSIC (`https://hdl.handle.net/10261/XXX`).
     - **Documentación Externa:** Enlaces a Python, Pandas, Matplotlib, GitHub, pyOpenSci.
   - Detectar enlaces mal formados, rotos o URLs locales no relativas.

3. **Verificación de Buenas Prácticas de Ciencia Abierta:**
   - Confirmar que los cuadernos utilicen datos abiertos en `DATASETS/`.
   - Verificar la ausencia de API keys explícitas (uso obligatorio de `load_dotenv()` y `.env`).
