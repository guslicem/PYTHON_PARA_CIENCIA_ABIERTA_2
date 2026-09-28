---
name: open-science-curator
description: Instrucciones especializadas para consultar el servidor OAI-PMH de Digital.CSIC, auditar licencias y generar citas BibTeX.
---

# Skill: Curador de Ciencia Abierta (CSIC)

## Protocolo de Actuación:
1. Recibir identificador persistente (DOI o Handle de Digital.CSIC).
2. Validar sintaxis con expresiones regulares (`re`).
3. Realizar petición HTTP al servidor OAI-PMH de Digital.CSIC (`https://digital.csic.es/dspace-oai/request?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:digital.csic.es:...`).
4. Extraer elementos Dublin Core (`dc:title`, `dc:creator`, `dc:date`, `dc:rights`).
5. Auditar concordancia con la política de Acceso Abierto del CSIC.
6. Formatear la cita resultante en BibTeX para manuscritos en LaTeX.
