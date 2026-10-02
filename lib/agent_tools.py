import re
import requests
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
    Utiliza BeautifulSoup para parsear el XML Dublin Core (oai_dc).
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
        
        titles = [t.text.strip() for t in soup.find_all("dc:title")]
        creators = [c.text.strip() for c in soup.find_all("dc:creator")]
        dates = [d.text.strip() for d in soup.find_all("dc:date")]
        rights = [r.text.strip() for r in soup.find_all("dc:rights")]
        types = [t.text.strip() for t in soup.find_all("dc:type")]
        
        return {
            "found": True,
            "handle": clean_handle,
            "title": titles[0] if titles else "Título no disponible",
            "authors": creators if creators else ["Autor no especificado"],
            "date": dates[0] if dates else "Sin fecha",
            "rights": rights if rights else ["No especificado"],
            "type": types[0] if types else "Documento científico",
            "oai_url": response.url
        }
    except Exception as e:
        return {"found": False, "error": f"Excepción durante la consulta OAI-PMH: {str(e)}"}

def tool_audit_open_access(rights_list: List[str]) -> Dict[str, Any]:
    """
    Audita los metadatos de derechos (dc:rights) para clasificar la política de Acceso Abierto.
    """
    rights_text = " ".join(rights_list).lower()
    
    is_open = any(kw in rights_text for kw in ["open access", "acceso abierto", "creative commons", "by", "mit", "public domain"])
    cc_license = "Desconocida"
    if "by-nc-nd" in rights_text:
        cc_license = "CC BY-NC-ND 4.0"
    elif "by-nc" in rights_text:
        cc_license = "CC BY-NC 4.0"
    elif "by" in rights_text or "creative commons" in rights_text:
        cc_license = "CC BY 4.0"
        
    return {
        "is_open_access": is_open,
        "license_detected": cc_license,
        "compliance_status": "CONFORME CSIC 2026" if is_open else "REVISIÓN MANUAL REQUERIDA",
        "raw_rights": rights_list
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
