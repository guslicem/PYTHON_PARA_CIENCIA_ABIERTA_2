import os
import re
import time
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

NREGS_TO_GENERATE = 250

def fetch_csic_metadata(handle):
    # SIEMPRE CORTESIA LO PRIMERO
    time.sleep(0.5)
    
    base_url = "https://digital.csic.es/dspace-oai/request"
    oai_id = f"oai:digital.csic.es:{str(handle).strip()}"
    params = {
        "verb": "GetRecord",
        "metadataPrefix": "oai_dc",
        "identifier": oai_id
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.content, "xml")
        if soup.find("error"):
            return None
        return soup
    except Exception:
        return None

def extract_doi_and_sdgs(soup):
    if soup is None:
        return "", [0]*17
    
    # 1. Extraer ExtDoi
    external_doi = ""
    for tag in soup.find_all(["dc:relation", "dc:identifier"]):
        txt = tag.get_text(strip=True)
        doi_match = re.search(r'10\.\d{4,9}/[^\s]+', txt, re.IGNORECASE)
        if doi_match:
            found_doi = doi_match.group(0).rstrip('.;,')
            # Excluir DOIs de Digital.CSIC (ej: 10.20350, 10.10261)
            if not re.search(r'(digitalcsic|10\.20350|10\.10261)', found_doi, re.IGNORECASE):
                external_doi = found_doi
                break
                
    # 2. Extraer SDG subjects (etiquetas ODS reales)
    sdg_labels = [0] * 17
    for tag in soup.find_all("dc:subject"):
        txt = tag.get_text(strip=True)
        sdg_match = re.search(r'metadata\.un\.org/sdg/(\d+)', txt)
        if sdg_match:
            sdg_num = int(sdg_match.group(1))
            if 1 <= sdg_num <= 17:
                sdg_labels[sdg_num - 1] = 1
                
    return external_doi, sdg_labels

def main():
    csv_path = "./DATASET/input_handles.csv"
    output_path = "./DATASET/test_batch_sample.csv"
    
    if not os.path.exists(csv_path):
        print(f"Error: No se encuentra el archivo {csv_path}")
        return
        
    df_handles = pd.read_csv(csv_path)
    handles = df_handles["handle"].dropna().unique().tolist()
    
    # Barajar aleatoriamente en cada ejecución
    random.shuffle(handles)
    
    print(f"Total de Handles únicos disponibles: {len(handles)}")
    print(f"Iniciando el muestreo de {NREGS_TO_GENERATE} registros con metadatos de Digital.CSIC...")
    print("Se aplica un tiempo de salvaguarda de 0.5 segundos entre peticiones por cortesía.")
    
    records = []
    attempts = 0
    pbar = tqdm(total=NREGS_TO_GENERATE)
    
    while len(records) < NREGS_TO_GENERATE and attempts < len(handles):
        handle = handles[attempts]
        attempts += 1
        
        soup = fetch_csic_metadata(handle)
        if soup is None:
            continue
            
        ext_doi, sdg_labels = extract_doi_and_sdgs(soup)
        
        record = {
            "Handle": handle,
            "ExtDoi": ext_doi if ext_doi else "NA"
        }
        # Agregar columnas SDG1 a SDG17 con las etiquetas reales
        for i, val in enumerate(sdg_labels):
            record[f"SDG{i+1}"] = val
            
        records.append(record)
        pbar.update(1)
        
    pbar.close()
    
    if len(records) < NREGS_TO_GENERATE:
        print(f"Advertencia: Solo se pudieron procesar {len(records)} registros.")
        
    df_output = pd.DataFrame(records)
    df_output.to_csv(output_path, index=False)
    print(f"\n¡Éxito! Archivo de prueba masiva guardado con éxito en: {output_path}")
    print(f"Registros guardados: {len(df_output)}")

if __name__ == "__main__":
    main()
