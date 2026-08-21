#!/usr/bin/env python3
"""
utils/export_notebooks_to_pdf.py
===============================================================================
Script de utilidad para exportar automáticamente todos los Cuadernos de Jupyter 
(.ipynb) ubicados en la carpeta NOTEBOOKS/ a formato PDF.

Uso:
    python utils/export_notebooks_to_pdf.py

Características:
    - Escanea la carpeta NOTEBOOKS/ buscando todos los archivos .ipynb.
    - Utiliza nbconvert con estrategia multiaspecto (webpdf, pdf latex, html fallback).
    - Muestra progreso dinámico en consola y reporte final de conversión.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple

# Definición de rutas relativas respecto a la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = BASE_DIR / "NOTEBOOKS"
OUTPUT_DIR = BASE_DIR / "doc" / "PDFS" / "NOTEBOOKS"


def find_notebooks(search_dir: Path) -> List[Path]:
    """Busca todos los cuadernos .ipynb dentro del directorio especificado, excluyendo temporales."""
    all_notebooks = list(search_dir.rglob("*.ipynb"))
    # Filtrar cuadernos en checkpoints de Jupyter o carpetas temporales de trabajo
    valid_notebooks = [
        nb for nb in all_notebooks 
        if ".ipynb_checkpoints" not in str(nb) and "scratch" not in str(nb)
    ]
    return sorted(valid_notebooks)

def convert_notebook_to_pdf(notebook_path: Path, output_dir: Path) -> Tuple[bool, str]:
    """
    Convierte un cuaderno individual a PDF utilizando jupyter nbconvert.
    Prueba progresivamente los motores: webpdf, pdf (LaTeX) e html como alternativa.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_filename = notebook_path.stem + ".pdf"
    target_pdf = output_dir / pdf_filename

    # Estrategia 1: Intentar exportación directa a webpdf (Chromium/Playwright)
    cmd_webpdf = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "webpdf",
        "--allow-chromium-download",
        "--disable-chromium-sandbox",
        str(notebook_path),
        "--output-dir", str(output_dir)
    ]
    
    try:
        res = subprocess.run(cmd_webpdf, capture_output=True, text=True, timeout=120)
        if res.returncode == 0 and target_pdf.exists():
            return True, f"✅ Exportado a PDF (webpdf): {pdf_filename}"
    except Exception:
        pass

    # Estrategia 2: Intentar exportación directa a pdf (XeLaTeX / pdflatex)
    cmd_pdf = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "pdf",
        str(notebook_path),
        "--output-dir", str(output_dir)
    ]
    try:
        res = subprocess.run(cmd_pdf, capture_output=True, text=True, timeout=120)
        if res.returncode == 0 and target_pdf.exists():
            return True, f"✅ Exportado a PDF (LaTeX): {pdf_filename}"
    except Exception:
        pass

    # Estrategia 3: Fallback a HTML enriquecido para conversión o impresión
    cmd_html = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "html",
        str(notebook_path),
        "--output-dir", str(output_dir)
    ]
    try:
        res = subprocess.run(cmd_html, capture_output=True, text=True, timeout=60)
        if res.returncode == 0:
            html_filename = notebook_path.stem + ".html"
            return False, f"⚠️ Generado HTML (instala xelatex o pyppeteer para PDF directo): {html_filename}"
    except Exception as e:
        return False, f"❌ Error convirtiendo {notebook_path.name}: {str(e)}"

    return False, f"❌ No se pudo generar PDF para {notebook_path.name}"

def main():
    print("=" * 75)
    print("📄 EXPORTADOR DE CUADERNOS JUPYTER A PDF - CURSO PYTHON CSIC")
    print("=" * 75)
    print(f"📁 Buscando cuadernos en: {NOTEBOOKS_DIR}")

    if not NOTEBOOKS_DIR.exists():
        print(f"❌ Error: La carpeta '{NOTEBOOKS_DIR}' no existe.")
        sys.exit(1)

    notebooks = find_notebooks(NOTEBOOKS_DIR)
    if not notebooks:
        print("⚠️ No se encontraron cuadernos (.ipynb) en la carpeta NOTEBOOKS/.")
        sys.exit(0)

    print(f"📊 Se han encontrado {len(notebooks)} cuadernos para procesar:\n")
    for idx, nb in enumerate(notebooks, 1):
        print(f"   {idx:02d}. {nb.relative_to(NOTEBOOKS_DIR)}")

    print(f"\n📂 Los archivos exportados se guardarán en: {OUTPUT_DIR}\n")
    print("-" * 75)

    exitos = 0
    advertencias = 0
    errores = 0

    for idx, nb in enumerate(notebooks, 1):
        print(f"🔄 [{idx}/{len(notebooks)}] Procesando: {nb.name} ...")
        exito, msg = convert_notebook_to_pdf(nb, OUTPUT_DIR)
        print(f"   {msg}")
        if exito:
            exitos += 1
        elif "HTML" in msg:
            advertencias += 1
        else:
            errores += 1

    print("\n" + "=" * 75)
    print("📊 RESUMEN DE LA EXPORTACIÓN")
    print("=" * 75)
    print(f"✅ PDFs generados con éxito: {exitos}")
    if advertencias > 0:
        print(f"⚠️ HTMLs alternativos generados: {advertencias}")
    if errores > 0:
        print(f"❌ Errores en conversión: {errores}")
    print(f"📁 Directorio de destino: {OUTPUT_DIR}")
    print("=" * 75)

if __name__ == "__main__":
    main()
