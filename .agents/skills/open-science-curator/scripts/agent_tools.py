import re
import requests
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
from typing import Dict, Any, List, Optional

def tool_validate_identifier(identifier: str) -> Dict[str, Any]:
    """
    Valida si la cadena ingresada es un DOI estándar o un Handle de Digital.CSIC.
    """
    clean_id = identifier.strip()
    
    doi_pattern = r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$"
    handle_pattern = r"^10261/\d+$"
    
    if re.match(handle_pattern, clean_id):
        return {
            "valid": True,
            "type": "Handle (Digital.CSIC)",
            "handle": clean_id,
            "oai_identifier": f"oai:digital.csic.es:{clean_id}",
            "url": f"https://hdl.handle.net/{clean_id}"
        }
    elif re.match(doi_pattern, clean_id):
        return {
            "valid": True,
            "type": "DOI",
            "doi": clean_id,
            "url": f"https://doi.org/{clean_id}"
        }
    else:
        return {
            "valid": False,
            "type": "Desconocido",
            "error": f"El identificador '{clean_id}' no cumple la sintaxis de Handle (10261/XXX) ni DOI."
        }

def tool_fetch_digital_csic_real(handle_id: str, timeout: int = 15) -> Dict[str, Any]:
    """
    Realiza una consulta HTTP REAL al protocolo OAI-PMH de Digital.CSIC para un Handle dado.
    Extrae explícitamente dc:rights y dc:rights.license.
    """
    clean_handle = handle_id.replace("https://hdl.handle.net/", "").replace("http://hdl.handle.net/", "").strip()
    if not clean_handle.startswith("10261/"):
        clean_handle = f"10261/{clean_handle}"
    
    oai_url = "https://digital.csic.es/dspace-oai/request"
    oai_identifier = f"oai:digital.csic.es:{clean_handle}"
    params = {
        "verb": "GetRecord",
        "metadataPrefix": "oai_dc",
        "identifier": oai_identifier
    }
    
    try:
        response = requests.get(oai_url, params=params, timeout=timeout)
        if response.status_code != 200:
            return {"found": False, "error": f"Error HTTP {response.status_code} desde Digital.CSIC"}
        
        soup = BeautifulSoup(response.text, "xml")
        
        error_tag = soup.find("error")
        if error_tag:
            return {"found": False, "error": f"Digital.CSIC OAI-PMH Error: {error_tag.text.strip()}"}
        
        titles = [t.text.strip() for t in soup.find_all("dc:title") if t.text.strip()]
        creators = [c.text.strip() for c in soup.find_all("dc:creator") if c.text.strip()]
        dates = [d.text.strip() for d in soup.find_all("dc:date") if d.text.strip()]
        types = [t.text.strip() for t in soup.find_all("dc:type") if t.text.strip()]
        
        # Búsqueda específica de dc:rights y dc:rights.license
        rights_tags = []
        license_tags = []

        for t in soup.find_all():
            name_lower = t.name.lower()
            text_val = t.text.strip()
            if not text_val:
                continue
            
            # Buscar dc.rights.license o qualificadores
            if "license" in name_lower or t.attrs.get("qualifier") == "license" or "rights.license" in name_lower:
                license_tags.append(text_val)
            # Buscar dc.rights (excluyendo license)
            elif name_lower in ["rights", "dc:rights", "dc.rights"] or ("rights" in name_lower and "license" not in name_lower):
                rights_tags.append(text_val)

        rights_list = rights_tags if rights_tags else ["dc.rights field identifier not found"]
        license_list = license_tags if license_tags else ["dc.rights.license Not found"]

        return {
            "found": True,
            "handle": clean_handle,
            "title": titles[0] if titles else "Título no disponible",
            "authors": creators if creators else ["Autor no especificado"],
            "date": dates[0] if dates else "Sin fecha",
            "year": dates[0][:4] if dates and dates[0][:4].isdigit() else "2026",
            "rights": rights_list,
            "rights_license": license_list,
            "type": types[0] if types else "Documento científico",
            "url": f"https://hdl.handle.net/{clean_handle}",
            "oai_url": response.url
        }
    except Exception as e:
        return {"found": False, "error": f"Excepción durante la consulta OAI-PMH: {str(e)}"}

def tool_audit_open_access(rights_list: List[str], license_list: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Audita los metadatos de derechos (dc:rights) y licencias (dc:rights.license) para clasificar el Acceso Abierto.
    """
    if license_list is None:
        license_list = ["dc.rights.license Not found"]

    rights_str = " ".join(rights_list)
    license_str = " ".join(license_list)

    has_rights = not any("dc.rights field identifier not found" in r.lower() for r in rights_list)
    has_license = not any("dc.rights.license not found" in l.lower() for l in license_list)

    # Caso en que no se encuentra ningún campo en el registro
    if not has_rights and not has_license:
        return {
            "is_open_access": False,
            "license_detected": "dc.rights.license Not found",
            "compliance_status": "dc.rights field identifier not found",
            "dc_rights": "dc.rights field identifier not found",
            "dc_rights_license": "dc.rights.license Not found"
        }

    combined_str = f"{rights_str} {license_str}".lower()

    is_closed = any(kw in combined_str for kw in ["closedaccess", "closed access", "restringido", "embargoed", "embargo"])
    is_open = any(kw in combined_str for kw in ["openaccess", "open access", "acceso abierto", "creative commons", "creativecommons", "public domain"]) or bool(re.search(r"\bby\b", combined_str))

    if is_closed:
        status = "ACCESO CERRADO / RESTRINGIDO"
        open_flag = False
    elif is_open:
        status = "CONFORME ACCESO ABIERTO (CSIC 2026)"
        open_flag = True
    else:
        status = "REVISIÓN MANUAL REQUERIDA"
        open_flag = False

    cc_license = "No especificada"
    if "by-nc-nd" in combined_str:
        cc_license = "CC BY-NC-ND 4.0"
    elif "by-nc-sa" in combined_str:
        cc_license = "CC BY-NC-SA 4.0"
    elif "by-nc" in combined_str:
        cc_license = "CC BY-NC 4.0"
    elif "by-sa" in combined_str:
        cc_license = "CC BY-SA 4.0"
    elif "by-nd" in combined_str:
        cc_license = "CC BY-ND 4.0"
    elif re.search(r"\bby\b", combined_str) or "creative commons" in combined_str or "creativecommons" in combined_str:
        cc_license = "CC BY 4.0"
    elif has_license:
        cc_license = license_list[0]
    elif open_flag:
        cc_license = "Open Access (eu-repo/semantics)"
    else:
        cc_license = license_list[0] if license_list else "dc.rights.license Not found"

    return {
        "is_open_access": open_flag,
        "license_detected": cc_license,
        "compliance_status": status,
        "dc_rights": ", ".join(rights_list),
        "dc_rights_license": ", ".join(license_list)
    }

def tool_format_bibtex(title: str, authors: List[str], year: str, handle: str) -> str:
    """
    Genera una entrada de cita bibliográfica en formato BibTeX listo para LaTeX.
    """
    first_author_surname = authors[0].split(",")[0].split()[-1].lower() if authors else "csic"
    clean_year = year[:4] if year and year[:4].isdigit() else "2026"
    bibkey = f"{first_author_surname}{clean_year}digitalcsic"
    
    formatted_authors = " and ".join(authors)
    
    bibtex = f"""@article{{{bibkey},
  title = {{{title}}},
  author = {{{formatted_authors}}},
  year = {{{clean_year}}},
  journal = {{Digital.CSIC Repository}},
  url = {{https://hdl.handle.net/{handle}}}
}}"""
    return bibtex

def tool_generate_summary_report(
    results: List[Dict[str, Any]], 
    author_name: str = "Gustavo Liñán Cembrano"
) -> Dict[str, Any]:
    """
    Genera un informe resumen estilizado en Markdown en ./doc/AGENT_REPORT/ con los resultados del análisis del agente.
    """
    now = datetime.now()
    timestamp_str = now.strftime("%Y%m%d_%H%M%S")
    date_display = now.strftime("%d/%m/%Y - %H:%M:%S")
    
    workspace_root = Path("/Users/linan/Desktop/RESEARCH/FORMACION/PYTHON_PARA_CIENCIA_ABIERTA_2")
    report_dir = workspace_root / "doc" / "AGENT_REPORT"
    report_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"Agent_Summary_Report_{timestamp_str}.md"
    file_path = report_dir / filename
    
    md_lines = []
    # Cabecera con Logo y Metadatos
    md_lines.append("![Logo Curso](../../assets/LogoCurso_gemini.png)")
    md_lines.append("")
    md_lines.append("# 📊 Informe de Auditoría y Curación de Ciencia Abierta")
    md_lines.append(f"**Curso:** Python para la Ciencia Abierta (CSIC 2026)  ")
    md_lines.append(f"**Creador del Reporte:** {author_name}  ")
    md_lines.append(f"**Fecha y Hora:** {date_display}  ")
    md_lines.append(f"**Total Registros Auditados:** {len(results)}  ")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    
    for idx, item in enumerate(results, 1):
        handle = item.get("handle", "N/A")
        md_lines.append(f"## 📌 Registro {idx:02d}: Handle `{handle}`")
        md_lines.append("")
        
        if item.get("found", False):
            md_lines.append(f"- **Título:** {item.get('title', 'Sin título')}")
            md_lines.append(f"- **Autores:** {', '.join(item.get('authors', []))}")
            md_lines.append(f"- **Año:** {item.get('year', 'N/A')}")
            md_lines.append(f"- **Enlace Institucional:** [{item.get('url', '')}]({item.get('url', '')})")
            
            audit = item.get("audit", item.get("audit_open_access", {}))
            status_symbol = "✅" if audit.get("is_open_access", False) else "⚠️"
            
            md_lines.append(f"- **dc.rights:** `{audit.get('dc_rights', item.get('rights', ['dc.rights field identifier not found'])[0])}`")
            md_lines.append(f"- **dc.rights.license:** `{audit.get('dc_rights_license', item.get('rights_license', ['dc.rights.license Not found'])[0])}`")
            md_lines.append(f"- **Estado Acceso Abierto:** {status_symbol} {audit.get('compliance_status', 'Conforme')}")
            md_lines.append(f"- **Licencia Detectada:** `{audit.get('license_detected', 'N/A')}`")
            
            bibtex = item.get("bibtex", "")
            if bibtex:
                md_lines.append("")
                md_lines.append("```bibtex")
                md_lines.append(bibtex)
                md_lines.append("```")
        else:
            md_lines.append(f"⚠️ **Error en la Consulta:** {item.get('error', 'Registro no encontrado')}")
            
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
        
    report_content = "\n".join(md_lines)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print(f"📄 [AGENTE]: Se ha creado exitosamente el informe de resumen en: '{file_path}'")
    
    return {
        "status": "success",
        "file_name": filename,
        "file_path": str(file_path),
        "total_records": len(results)
    }
