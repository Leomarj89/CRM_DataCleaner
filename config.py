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

ALIAS_COLUMNAS = {

    "nombre": [
        "nombre",
        "nombres",
    ],

    "apellido": [
        "apellido",
        "apellidos",
    ],

    "correo": [
        "correo",
        "correoelectronico",
        "email",
        "emailpersonal",
        "emailcontacto",
        "mail",
        "correoempresa",
        "correopersonal",
    ],

    "teléfono": [
        "telefono",
        "telefono1",
        "telefono2",
        "celular",
        "movil",
        "fono",
        "whatsapp",
    ],

    "profesión": [
        "profesion",
        "ocupacion",
    ],

    "cargo": [
        "cargo",
        "puesto",
    ],

    "institución": [
        "institucion",
        "empresa",
        "organizacion",
        "establecimiento",
        "colegio",
        "escuela",
    ],

    "segmento": [
        "segmento",
    ],

    "estado": [
        "estado",
    ],
}

# ======================================================
# Patrones de limpieza
# ======================================================

PATRONES_PROFESION = [
    r"\(A\)",
    r"\(O\)",
    r"\(AS\)",
    r"\(OS\)",
    r"\bPIE\b",
]

PATRONES_INSTITUCION = [

]

PATRONES_CARGO = [

]

REEMPLAZOS_PROFESION = {
    "PSICOLOGA": "PSICOLOGO",
}