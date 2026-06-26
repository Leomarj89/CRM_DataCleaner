from rich.console import Console
from rich.table import Table

console = Console()


class InspectorDataFrame:
    """
    Analiza un DataFrame sin modificarlo.

    Su objetivo es obtener información útil sobre la calidad
    de los datos antes de iniciar cualquier proceso de limpieza.
    """

    def __init__(self, dataframe, nombre_archivo):

        self.df = dataframe
        self.nombre_archivo = nombre_archivo

    # -------------------------------------------------

    def obtener_dimensiones(self):
        """
        Devuelve la cantidad de filas y columnas del DataFrame.
        """

        filas, columnas = self.df.shape

        return filas, columnas

    # -------------------------------------------------

    def mostrar_resumen_general(self):
        """
        Muestra un resumen general del archivo cargado.
        """

        filas, columnas = self.obtener_dimensiones()

        tabla = Table(title="Resumen General")

        tabla.add_column("Propiedad", style="cyan")
        tabla.add_column("Valor", style="green")

        tabla.add_row("Archivo", self.nombre_archivo)
        tabla.add_row("Filas", str(filas))
        tabla.add_row("Columnas", str(columnas))

        console.print()
        console.print(tabla)

    # -------------------------------------------------

    def ejecutar(self):
        """
        Ejecuta la inspección básica.
        """

        self.mostrar_resumen_general()