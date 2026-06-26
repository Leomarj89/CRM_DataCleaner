from config import (
    CARPETA_ENTRADA,
    CARPETA_SALIDA,
    CARPETA_LOGS,
    CARPETA_DATOS
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