from config import (
    CARPETA_ENTRADA,
    CARPETA_SALIDA,
    CARPETA_LOGS,
    CARPETA_DATOS
)

from unidecode import unidecode


def normalizar_texto(texto: str) -> str:
    """
    Normaliza un texto para facilitar comparaciones.

    Convierte a minúsculas, elimina acentos y espacios.

    Args:
        texto: Texto a normalizar.

    Returns:
        str: Texto normalizado.
    """

    return (
        unidecode(texto)
        .lower()
        .replace(" ", "")
        .replace("_", "")
        .replace("-", "")
        .replace(".", "")
        .replace(",", "")
        .replace(":", "")
        .replace(";", "")
        .replace("(", "")
        .replace(")", "")
    )

def crear_carpetas():

    for carpeta in [

        CARPETA_ENTRADA,

        CARPETA_SALIDA,

        CARPETA_LOGS,

        CARPETA_DATOS

    ]:

        carpeta.mkdir(
            exist_ok=True
        )