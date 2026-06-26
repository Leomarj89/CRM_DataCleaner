from pathlib import Path

# ======================================================
# Información del proyecto
# ======================================================

NOMBRE_PROYECTO = "CRM Data Cleaner"
VERSION = "1.0.0"

# ======================================================
# Rutas
# ======================================================

ROOT = Path(__file__).parent

CARPETA_ENTRADA = ROOT / "entrada"
CARPETA_SALIDA = ROOT / "salida 25.06.2026"
CARPETA_DATOS = ROOT / "datos"
CARPETA_LOGS = ROOT / "logs"

# ======================================================
# Archivos
# ======================================================

DICCIONARIO_PROFESIONES = (
    CARPETA_DATOS / "diccionario_profesiones.json"
)

# ======================================================
# Configuración
# ======================================================

ENCODINGS = [
    "utf-8",
    "utf-8-sig",
    "latin1"
]

EXTENSIONES_PERMITIDAS = [
    ".csv",
    ".xlsx"
]