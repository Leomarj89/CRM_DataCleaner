from rich.console import Console

from src.banner import mostrar_banner
from src.logger import logger
from src.utilidades import crear_carpetas
from src.lector import LectorCSV
from src.inspector import InspectorDataFrame

console = Console()


def main():

    mostrar_banner()

    crear_carpetas()

    logger.info("Proyecto iniciado.")

    # -------------------------------
    # Lectura del archivo
    # -------------------------------

    lector = LectorCSV()

    df = lector.ejecutar()

    logger.info(
        f"Archivo cargado correctamente. "
        f"Filas: {df.shape[0]}"
    )

    # -------------------------------
    # Inspección del DataFrame
    # -------------------------------

    inspector = InspectorDataFrame(
        dataframe=df,
        nombre_archivo=lector.archivo.name
    )

    inspector.ejecutar()

    console.print()

    console.print(
        "[bold green]✔ Sprint 3 completado correctamente[/]"
    )

    console.print()


if __name__ == "__main__":
    main()