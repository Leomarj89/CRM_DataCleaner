from pathlib import Path

import pandas as pd

from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt

from config import (
    CARPETA_ENTRADA,
    ENCODINGS,
    EXTENSIONES_PERMITIDAS
)

console = Console()


class LectorCSV:
    """
    Clase encargada de localizar y leer archivos
    CSV y Excel.
    """

    def __init__(self):

        self.carpeta = CARPETA_ENTRADA
        self.archivo = None
        self.df = None
        self.encoding = None

    # -------------------------------------------------

    def buscar_archivos(self):

        archivos = []

        for extension in EXTENSIONES_PERMITIDAS:

            archivos.extend(
                self.carpeta.glob(f"*{extension}")
            )

        return sorted(archivos)

    # -------------------------------------------------

    def mostrar_archivos(self, archivos):

        tabla = Table(
            title="Archivos encontrados"
        )

        tabla.add_column(
            "N°",
            justify="center"
        )

        tabla.add_column(
            "Archivo"
        )

        for i, archivo in enumerate(archivos, start=1):

            tabla.add_row(
                str(i),
                archivo.name
            )

        console.print(tabla)

    # -------------------------------------------------

    def seleccionar_archivo(self, archivos):

        while True:

            opcion = IntPrompt.ask(
                "\nSeleccione un archivo"
            )

            if 1 <= opcion <= len(archivos):

                self.archivo = archivos[opcion - 1]

                return

            console.print(
                "\n[red]Opción inválida[/]"
            )

    # -------------------------------------------------

    def detectar_encoding(self):

        if self.archivo.suffix == ".xlsx":

            self.encoding = None

            return

        for encoding in ENCODINGS:

            try:

                pd.read_csv(
                    self.archivo,
                    encoding=encoding,
                    nrows=5
                )

                self.encoding = encoding

                return

            except Exception:

                pass

        raise Exception(
            "No fue posible detectar el encoding."
        )

    # -------------------------------------------------

    def leer_archivo(self):

        if self.archivo.suffix == ".csv":

            self.df = pd.read_csv(
                self.archivo,
                encoding=self.encoding
            )

        else:

            self.df = pd.read_excel(
                self.archivo
            )

    # -------------------------------------------------

    def mostrar_resumen(self):

        tabla = Table(
            title="Resumen del archivo"
        )

        tabla.add_column("Propiedad")
        tabla.add_column("Valor")

        tabla.add_row(
            "Archivo",
            self.archivo.name
        )

        tabla.add_row(
            "Tipo",
            self.archivo.suffix
        )

        tabla.add_row(
            "Encoding",
            self.encoding or "No aplica"
        )

        tabla.add_row(
            "Filas",
            str(self.df.shape[0])
        )

        tabla.add_row(
            "Columnas",
            str(self.df.shape[1])
        )

        console.print()
        console.print(tabla)

        console.print("\n[cyan]Columnas encontradas:[/]\n")

        for columna in self.df.columns:

            console.print(
                f"   • {columna}"
            )

    # -------------------------------------------------

    def ejecutar(self):

        archivos = self.buscar_archivos()

        if not archivos:

            raise FileNotFoundError(
                "No existen archivos en la carpeta entrada."
            )

        self.mostrar_archivos(archivos)

        self.seleccionar_archivo(archivos)

        self.detectar_encoding()

        self.leer_archivo()

        self.mostrar_resumen()

        return self.df