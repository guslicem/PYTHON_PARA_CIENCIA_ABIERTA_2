"""
Librería para la Lectura y Extracción de Registros de Digital.CSIC a partir de Handles
=======================================================================================

Módulo de Python diseñado para consultar el protocolo OAI-PMH del repositorio institucional
Digital.CSIC y recuperar metadatos bibliográficos completos de publicaciones científicas.

Autor: Gustavo Liñán (Gustavo.Linan@csic.es)
Institución: Consejo Superior de Investigaciones Científicas (CSIC)
Licencia: MIT License

Ejemplo de uso rápido:
----------------------
>>> import digital_csic as dcsic
>>> # 1. Consultar un registro individual por Handle
>>> record = dcsic.fetch_digital_csic_record("10261/2008")
>>> print(record['title'])
>>>
>>> # 2. Cargar una lista de Handles y procesar masivamente en un DataFrame de pandas
>>> handles = dcsic.load_handles_from_file("DATASET/input_handles.csv")
>>> df_records = dcsic.fetch_records_batch(handles[:10], max_workers=4)
>>> dcsic.export_records_to_csv(df_records, "registros_digital_csic.csv")
"""

import os
import re
import time
import logging
from typing import List, Dict, Optional, Union
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("DigitalCSICReader")

# URL base del servicio OAI-PMH de Digital.CSIC
DIGITAL_CSIC_OAI_URL = "https://digital.csic.es/dspace-oai/request"


def normalize_handle(handle_input: str) -> Optional[str]:
    """
    Normaliza y extrae un Handle válido de Digital.CSIC a partir de diversos formatos de entrada.

    Soporta entradas como:
    - `"10261/2008"`
    - `"http://hdl.handle.net/10261/2008"`
    - `"https://digital.csic.es/handle/10261/2008"`
    - `"hdl_10261_2008"`

    Args:
        handle_input (str): Cadena de texto que contiene el Handle o URL.

    Returns:
        Optional[str]: El Handle formateado como `"10261/XXXXX"` o `None` si no es válido.

    Example:
        >>> normalize_handle("http://hdl.handle.net/10261/2008")
        '10261/2008'
    """
    if not handle_input or not isinstance(handle_input, str):
        return None

    # Buscar el patrón estándar 10261/<ID_numérico>
    match = re.search(r'10261/\d+', handle_input, re.IGNORECASE)
    if match:
        return match.group(0)

    # Si viene delimitado por guiones o guiones bajos (ej: 10261_2008)
    alt_match = re.search(r'10261[-_](\d+)', handle_input, re.IGNORECASE)
    if alt_match:
        return f"10261/{alt_match.group(1)}"

    return None


def fetch_external_doi_metadata(doi: str, timeout: int = 10) -> Optional[Dict[str, str]]:
    """
    Consulta servicios externos de metadatos (Crossref API) para enriquecer la información
    de un artículo cuando el abstract en Digital.CSIC no está disponible o es insuficiente.

    Args:
        doi (str): Identificador Digital de Objeto (DOI) del artículo.
        timeout (int, optional): Tiempo máximo de espera para la petición HTTP en segundos. Defaults to 10.

    Returns:
        Optional[Dict[str, str]]: Diccionario con metadatos (`title`, `abstract`, `authors`, `year`, `journal`)
                                  o `None` si la consulta falla.

    Example:
        >>> metadata = fetch_external_doi_metadata("10.1016/j.jcp.2020.109500")
    """
    clean_doi = doi.strip()
    if not clean_doi:
        return None

    url = f"https://api.crossref.org/works/{clean_doi}"
    headers = {"User-Agent": "DigitalCSICLibrary/1.0 (mailto:Gustavo.Linan@csic.es)"}

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        if response.status_code != 200:
            return None

        item = response.json().get("message", {})

        # Título
        titles = item.get("title", [])
        title = titles[0] if titles else ""

        # Autores
        authors_list = [
            f"{a.get('given', '')} {a.get('family', '')}".strip()
            for a in item.get("author", [])
        ]
        authors = ", ".join(authors_list)

        # Año de publicación
        year = ""
        date_parts = item.get("published", {}).get("date-parts", [[]])[0]
        if date_parts:
            year = str(date_parts[0])

        # Abstract (limpiar etiquetas HTML/XML)
        abstract_raw = item.get("abstract", "")
        abstract = re.sub(r'<[^>]+>', '', abstract_raw).strip()

        # Revista / Fuente
        journal_list = item.get("container-title", [])
        journal = journal_list[0] if journal_list else ""

        return {
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "year": year,
            "journal": journal
        }

    except Exception as e:
        logger.debug("Error al consultar DOI externo %s en Crossref: %s", clean_doi, e)
        return None


def fetch_digital_csic_record(
    handle_input: str,
    timeout: int = 15,
    enrich_external: bool = True
) -> Optional[Dict[str, str]]:
    """
    Recupera los metadatos de una publicación desde el servidor OAI-PMH de Digital.CSIC dado su Handle.

    Extrae los campos principales (`title`, `abstract`, `authors`, `year`, `journal`, `doi`)
    y opcionalmente consulta fuentes externas para completar resúmenes faltantes.

    Args:
        handle_input (str): El Handle o URL del registro en Digital.CSIC (ej. `"10261/2008"`).
        timeout (int, optional): Tiempo límite de espera HTTP en segundos. Defaults to 15.
        enrich_external (bool, optional): Si se debe consultar un DOI externo en Crossref cuando
                                           falte el abstract. Defaults to True.

    Returns:
        Optional[Dict[str, str]]: Diccionario con las siguientes claves:
            - `handle`: Handle normalizado.
            - `title`: Título de la obra.
            - `abstract`: Resumen / Descripción.
            - `authors`: Lista de autores separados por coma.
            - `year`: Año de publicación.
            - `journal`: Nombre de la revista o fuente.
            - `doi`: DOI detectado (externo o handle).
            - `source`: Cadena identificadora del origen ("Digital.CSIC (Handle)").
            Retorna `None` si el Handle es inválido o no se puede recuperar el registro.

    Example:
        >>> rec = fetch_digital_csic_record("10261/2008")
        >>> print(rec['title'])
        'El materialismo histórico como programa de investigación.'
    """
    handle = normalize_handle(handle_input)
    if not handle:
        logger.warning("Handle inválido proporcionado: '%s'", handle_input)
        return None

    oai_id = f"oai:digital.csic.es:{handle}"
    params = {
        "verb": "GetRecord",
        "metadataPrefix": "oai_dc",
        "identifier": oai_id
    }

    try:
        response = requests.get(DIGITAL_CSIC_OAI_URL, params=params, timeout=timeout)
        if response.status_code != 200:
            logger.warning("Respuesta HTTP %d al consultar OAI-PMH para %s", response.status_code, handle)
            return None
    except Exception as e:
        logger.error("Error de conexión al consultar Digital.CSIC para %s: %s", handle, e)
        return None

    # Parsear respuesta XML
    soup = BeautifulSoup(response.content, "xml")
    if soup.find("error"):
        logger.warning("OAI-PMH retornó error para el handle %s", handle)
        return None

    # 1. Título (priorizar idioma español)
    titles = soup.find_all("dc:title")
    title = ""
    for t in titles:
        txt = t.get_text(" ", strip=True)
        lang = (t.get("xml:lang") or "").lower()
        if txt and lang.startswith("es"):
            title = txt
            break
    if not title and titles:
        title = next((t.get_text(" ", strip=True) for t in titles if t.get_text(strip=True)), "")

    # 2. Resumen / Abstract (priorizar español y filtrar notas de evaluación de pares)
    desc_tags = soup.find_all("dc:description")
    candidates = []
    for d in desc_tags:
        txt = d.get_text(" ", strip=True)
        if not txt or txt.lower().startswith("peer reviewed"):
            continue
        lang = (d.get("xml:lang") or "").lower()
        priority = 0 if lang.startswith("es") else 1
        candidates.append((priority, txt))
    candidates.sort(key=lambda x: x[0])

    seen = set()
    ordered_descriptions = []
    for _, txt in candidates:
        if txt not in seen:
            seen.add(txt)
            ordered_descriptions.append(txt)
    abstract = " ".join(ordered_descriptions) if ordered_descriptions else ""
    if len(abstract) > 12000:
        abstract = abstract[:12000]

    # 3. Autores (dc:creator)
    creators = [c.get_text(" ", strip=True) for c in soup.find_all("dc:creator") if c.get_text(strip=True)]
    authors = ", ".join(creators)

    # 4. Año de publicación (dc:date)
    year = ""
    for d in soup.find_all("dc:date"):
        txt = d.get_text(strip=True)
        y_match = re.search(r'\b(19\d\d|20\d\d)\b', txt)
        if y_match:
            year = y_match.group(1)
            break

    # 5. Revista / Editorial / Fuente (dc:publisher o dc:source)
    journal = ""
    pub_tag = soup.find("dc:publisher") or soup.find("dc:source")
    if pub_tag:
        journal = pub_tag.get_text(" ", strip=True)

    # 6. Identificación de DOI externo
    external_doi = ""
    for tag in soup.find_all(["dc:relation", "dc:identifier"]):
        txt = tag.get_text(strip=True)
        doi_match = re.search(r'10\.\d{4,9}/[^\s]+', txt, re.IGNORECASE)
        if doi_match:
            found_doi = doi_match.group(0).rstrip('.;,')
            # Excluir DOIs internos o de repositorio de Digital.CSIC
            if not re.search(r'(digitalcsic|10\.20350|10\.10261)', found_doi, re.IGNORECASE):
                external_doi = found_doi
                break

    # 7. Enriquecimiento con DOI externo si falta el abstract
    if enrich_external and (not abstract or len(abstract.strip()) < 20 or abstract.lower() == "sin abstract") and external_doi:
        logger.debug("Handle %s sin abstract en Digital.CSIC. Enriqueciendo vía DOI externo: %s", handle, external_doi)
        doi_meta = fetch_external_doi_metadata(external_doi)
        if doi_meta:
            if not title or title.lower() == "sin título":
                title = doi_meta.get("title", title)
            if doi_meta.get("abstract") and doi_meta["abstract"].lower() != "sin abstract":
                abstract = doi_meta["abstract"]
            if not authors:
                authors = doi_meta.get("authors", authors)
            if not year:
                year = doi_meta.get("year", year)
            if not journal:
                journal = doi_meta.get("journal", journal)

    return {
        "handle": handle,
        "title": title or "Sin título",
        "abstract": abstract or "Sin abstract disponible",
        "authors": authors or "Autores no especificados",
        "year": year or "",
        "journal": journal or "Digital.CSIC",
        "doi": external_doi or f"10261/{handle.split('/')[-1]}",
        "source": "Digital.CSIC (Handle)"
    }


def fetch_records_batch(
    handles: List[str],
    max_workers: int = 5,
    delay: float = 0.05,
    show_progress: bool = True
) -> pd.DataFrame:
    """
    Procesa de manera concurrente una lista de Handles de Digital.CSIC y devuelve un DataFrame de pandas.

    Utiliza `ThreadPoolExecutor` para acelerar las peticiones de red sin saturar el servidor objetivo.

    Args:
        handles (List[str]): Lista de cadenas con Handles o URLs de Digital.CSIC.
        max_workers (int, optional): Número de hilos concurrentes para peticiones HTTP. Defaults to 5.
        delay (float, optional): Pausa entre peticiones en segundos para control de tasa (throttling). Defaults to 0.05.
        show_progress (bool, optional): Muestra una barra de progreso en consola si está disponible. Defaults to True.

    Returns:
        pd.DataFrame: DataFrame estructurado con las columnas:
                      `['handle', 'title', 'abstract', 'authors', 'year', 'journal', 'doi', 'source']`.

    Example:
        >>> df = fetch_records_batch(["10261/2008", "10261/4108"], max_workers=2)
        >>> df.head()
    """
    clean_handles = [h for h in (normalize_handle(h) for h in handles) if h]
    records = []
    total = len(clean_handles)

    if total == 0:
        logger.warning("No se proporcionaron Handles válidos para procesar.")
        return pd.DataFrame(columns=['handle', 'title', 'abstract', 'authors', 'year', 'journal', 'doi', 'source'])

    logger.info("Iniciando procesamiento masivo de %d registros de Digital.CSIC (%d hilos)...", total, max_workers)

    # Intentar usar tqdm para barra de progreso si está instalado
    try:
        from tqdm import tqdm
        progress_bar = tqdm(total=total, desc="Digital.CSIC", disable=not show_progress)
    except ImportError:
        progress_bar = None

    def worker(handle_str: str) -> Optional[Dict[str, str]]:
        if delay > 0:
            time.sleep(delay)
        return fetch_digital_csic_record(handle_str, enrich_external=True)

    completed = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_handle = {executor.submit(worker, h): h for h in clean_handles}

        for future in as_completed(future_to_handle):
            rec = future.result()
            if rec:
                records.append(rec)

            completed += 1
            if progress_bar:
                progress_bar.update(1)
            elif show_progress and completed % max(1, total // 10) == 0:
                logger.info("Progreso: %d/%d (%.1f%%)", completed, total, (completed / total) * 100)

    if progress_bar:
        progress_bar.close()

    df = pd.DataFrame(records)
    cols = ['handle', 'title', 'abstract', 'authors', 'year', 'journal', 'doi', 'source']
    for col in cols:
        if col not in df.columns:
            df[col] = ""

    logger.info("Procesamiento finalizado. Registros recuperados exitosamente: %d/%d", len(df), total)
    return df[cols]


def load_handles_from_file(file_path: str, column_name: str = "handle") -> List[str]:
    """
    Carga una lista de Handles desde un archivo de texto (.txt), archivo CSV (.csv) o Excel (.xlsx/.xls).
    Soporta rutas relativas desde distintas ubicaciones del proyecto.
    """
    target_path = file_path
    if not os.path.exists(target_path):
        # Probar rutas relativas alternativas comunes (desde NOTEBOOKS/ o desde la raíz)
        alt_paths = [
            os.path.join("..", file_path),
            os.path.join("DATASETS", "FROM_DIGITALCSIC", "input_handles.csv"),
            os.path.join("..", "DATASETS", "FROM_DIGITALCSIC", "input_handles.csv")
        ]
        found = False
        for alt in alt_paths:
            if os.path.exists(alt):
                target_path = alt
                found = True
                break
        if not found:
            raise FileNotFoundError(f"El archivo especificado no existe: {file_path}")

    ext = os.path.splitext(target_path)[1].lower()

    if ext in [".csv", ".tsv"]:
        sep = "\t" if ext == ".tsv" else ","
        df = pd.read_csv(target_path, sep=sep)
        # Buscar columna objetivo insensible a mayúsculas
        matched_col = next((c for c in df.columns if str(c).strip().lower() == column_name.lower()), df.columns[0])
        handles_raw = df[matched_col].dropna().astype(str).tolist()

    elif ext in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)
        matched_col = next((c for c in df.columns if str(c).strip().lower() == column_name.lower()), df.columns[0])
        handles_raw = df[matched_col].dropna().astype(str).tolist()

    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            handles_raw = [line.strip() for line in f if line.strip()]
    else:
        raise ValueError(f"Formato de archivo no soportado: '{ext}'. Use .csv, .txt o .xlsx")

    handles = [norm for norm in (normalize_handle(h) for h in handles_raw) if norm]
    logger.info("Cargados %d Handles válidos desde '%s'", len(handles), file_path)
    return handles


def export_records_to_csv(df: pd.DataFrame, output_path: str, index: bool = False) -> str:
    """
    Exporta el DataFrame de registros a un archivo CSV codificado en UTF-8 con BOM (utf-8-sig)
    para máxima compatibilidad con Microsoft Excel y la aplicación web de procesamiento en lote.

    Args:
        df (pd.DataFrame): DataFrame con los metadatos de los registros.
        output_path (str): Ruta de destino para guardar el archivo CSV.
        index (bool, optional): Incluir el índice de pandas en el CSV. Defaults to False.

    Returns:
        str: Ruta absoluta del archivo CSV exportado.

    Example:
        >>> export_records_to_csv(df, "salida_digital_csic.csv")
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    df.to_csv(output_path, index=index, encoding="utf-8-sig")
    abs_path = os.path.abspath(output_path)
    logger.info("Archivo CSV guardado exitosamente en: %s", abs_path)
    return abs_path


def GeneraAPA(response: Union[requests.Response, str, BeautifulSoup]) -> str:
    """
    Pequeña función para generar una cita bibliográfica tipo formato APA a partir
    de autores, título, revista/fuente, DOI e identificador Handle.

    Uso:
    >>> APA_TEXT = dcsic.GeneraAPA(response)

    Argumentos:
        response (Union[requests.Response, str, BeautifulSoup]):
            Objeto respuesta HTTP de requests, cadena XML o BeautifulSoup devuelto tras consultar
            params = {"verb": "GetRecord", "metadataPrefix": "oai_dc", "identifier": oai_id}

    Autor: Gustavo.Linan@csic.es
    """
    if isinstance(response, BeautifulSoup):
        r = response
    elif hasattr(response, "text"):
        r = BeautifulSoup(response.text, "xml")
    elif isinstance(response, str):
        r = BeautifulSoup(response, "xml")
    else:
        raise ValueError("Se esperaba un objeto Response de requests, BeautifulSoup o texto XML.")

    # --- Título ---
    titulo_tag = r.find("dc:title")
    titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"

    # --- Autores ---
    autores = r.find_all("dc:creator")
    autores_lista = ", ".join([a.text.strip() for a in autores]) if autores else "Autor desconocido"

    # --- Identificadores ---
    identifier_tags = r.find_all("identifier")
    journal = None
    doi = "No disponible"
    handle = "No disponible"

    for tag in identifier_tags:
        texto = tag.text.strip()
        lower = texto.lower()

        if texto.startswith("oai:"):
            continue  # saltar el identificador OAI, no nos interesa

        if "doi.org" in lower:
            doi = texto
        elif lower.startswith("10."):
            doi = f"https://doi.org/{texto}"
        elif "hdl.handle.net" in lower:
            handle = texto
        elif not journal and ("(" in texto and ")" in texto):
            # heurística: probable referencia bibliográfica
            journal = texto

    if journal is None:
        journal = "No disponible"

    return f"{autores_lista}, {titulo}, {journal}, {doi}, {handle}"


# --- Bloque de Demostración / Ejemplo de Uso ---
if __name__ == "__main__":
    print("=" * 70)
    print(" Demostración de la librería Digital.CSIC Reader")
    print("=" * 70)

    # 1. Ejemplo con un Handle individual
    sample_handle = "10261/2008"
    print(f"\n[1] Consultando registro individual para Handle: {sample_handle}...")
    rec = fetch_digital_csic_record(sample_handle)
    if rec:
        print(f"  - Título  : {rec['title']}")
        print(f"  - Autores : {rec['authors']}")
        print(f"  - Año     : {rec['year']}")
        print(f"  - Fuente  : {rec['journal']}")
        print(f"  - DOI     : {rec['doi']}")

    # 2. Ejemplo con carga desde CSV si existe
    csv_sample_path = os.path.join("DATASET", "input_handles.csv")
    if os.path.exists(csv_sample_path):
        print(f"\n[2] Leyendo Handles desde '{csv_sample_path}'...")
        handles_list = load_handles_from_file(csv_sample_path)
        print(f"  - Total Handles leídos: {len(handles_list)}")

        # Tomar los primeros 5 Handles para demostración rápida
        test_handles = handles_list[:5]
        print(f"\n[3] Extrayendo metadatos en lote para 5 Handles: {test_handles}...")
        df_results = fetch_records_batch(test_handles, max_workers=3)

        out_csv = "DATASET/demo_digital_csic_output.csv"
        export_records_to_csv(df_results, out_csv)
        print("\nPrimeras filas extraídas:")
        print(df_results[['handle', 'title', 'year', 'doi']].to_string())
    print("\n¡Demostración completada!")
