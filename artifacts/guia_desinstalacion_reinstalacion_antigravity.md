# Guía de Desinstalación Limpia y Reinstalación de Antigravity-IDE en macOS

**Destinatario:** Gustavo (guslicem@gmail.com)  
**Curso:** Python para Ciencia Abierta (CSIC / Universidad)

---

## Parte 1: Desinstalación Limpia (Eliminación Completa de Rastros y Cachés)

Ejecuta los siguientes comandos en la **Terminal de Mac** para borrar la aplicación, configuraciones y cachés previas:

```bash
# 1. Eliminar la aplicación
sudo rm -rf "/Applications/Antigravity IDE.app" "/Applications/Antigravity.app"

# 2. Eliminar directorios de configuración, agentes y datos de usuario
rm -rf ~/.antigravity-ide
rm -rf ~/.antigravity
rm -rf ~/Library/Application\ Support/Antigravity*
rm -rf ~/Library/Caches/com.google.antigravity*
rm -rf ~/Library/Preferences/com.google.antigravity*
rm -rf ~/Library/Saved\ Application\ State/com.google.antigravity*.savedState
```

---

## Parte 2: Reinstalación y Configuración Limpia (3 Pasos)

### Paso 1: Descarga e Instalación del IDE
1. Descarga el paquete de instalación oficial para macOS (Apple Silicon / Intel) desde el portal de Google Antigravity:  
   👉 **https://antigravity.google**
2. Arrastra la aplicación **Antigravity IDE** a la carpeta **Aplicaciones**.

### Paso 2: Preparación del Entorno Virtual del Proyecto
Abre la Terminal en la carpeta raíz del proyecto (`PYTHON_PARA_CIENCIA_ABIERTA_2`) y ejecuta:

```bash
# Crear entorno virtual limpio
python3 -m venv venv

# Actualizar pip e instalar dependencias del curso
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

# Registrar el Kernel de Jupyter para el alumnado
./venv/bin/python -m ipykernel install --user --name python-ciencia-abierta --display-name "Python 3 (Ciencia Abierta - venv)"
```

### Paso 3: Abrir Antigravity-IDE y Verificar Autocompletado
1. Abre **Antigravity IDE** y selecciona **File ➔ Open Folder...** eligiendo la carpeta del proyecto `PYTHON_PARA_CIENCIA_ABIERTA_2`.
2. Al abrir el proyecto, la carpeta preconfigurada `.vscode/settings.json` activará automáticamente:
   - El intérprete de Python en `./venv/bin/python`.
   - Las sugerencias en línea (*Ghost Text*) en `.py` y `.ipynb`.
3. Para ejecutar un cuaderno Jupyter (`NOTEBOOKS/WIP/15_Autocompletado_Inteligente_con_IA.ipynb`):
   - En la esquina superior derecha del cuaderno, haz clic en **Select Kernel** ➔ **Python Environments...** ➔ Selecciona **`Python 3 (Ciencia Abierta - venv)`**.
   - Haz clic en cualquier celda de código y pulsa **`Cmd + I`** o **`Cmd + K`** para invocar el asistente de IA.

---

*Documento generado para la preparación docente del curso Python para Ciencia Abierta.*
