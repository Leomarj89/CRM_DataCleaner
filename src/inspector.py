from rich.console import Console
from rich.table import Table
import pandas as pd

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

    def obtener_tipos(self) -> pd.Series:
        """
        Obtiene el tipo de dato de cada columna del DataFrame.

        Returns:
        pd.Series: Serie con los tipos de datos por columna.
        """
        return self.df.dtypes
    
    # -------------------------------------------------

    def mostrar_tipos(self) -> None:
        """
        Muestra los tipos de datos de cada columna en una tabla.
        """

        tipos = self.obtener_tipos()

        tabla = Table(
            title="Tipos de datos",
            show_header=True,
            header_style="bold cyan"
    )

        tabla.add_column("Columna", style="green")
        tabla.add_column("Tipo", style="yellow")

        for columna, tipo in tipos.items():
            tabla.add_row(columna, str(tipo))

        console.print(tabla)

    # -------------------------------------------------

    def obtener_nulos(self) -> pd.Series:
        """
        Obtiene la cantidad de valores nulos por columna.

        Returns:
        pd.Series: Serie con la cantidad de valores nulos por columna.
        """
        return self.df.isna().sum()
    
    # -------------------------------------------------

    def mostrar_nulos(self) -> None:
        """
        Muestra la cantidad y porcentaje de valores nulos por columna.
        """

        nulos = self.obtener_nulos()
        total_filas = len(self.df)

        tabla = Table(
            title="Valores nulos",
            show_header=True,
            header_style="bold cyan",
        )

        tabla.add_column("Columna", style="green")
        tabla.add_column("Nulos", justify="right")
        tabla.add_column("% Nulos", justify="right")

        for columna, cantidad in nulos.items():

            porcentaje = (cantidad / total_filas) * 100

            if porcentaje == 0:
                color = "green"
            elif porcentaje <= 5:
                color = "yellow"
            else:
                color = "red"

            tabla.add_row(
                columna,
                str(cantidad),
                f"[{color}]{porcentaje:.1f}%[/{color}]",
            )

        console.print(tabla)
    
    # ------------------------------------------------

    def obtener_unicos(self) -> pd.DataFrame:
        """
        Obtiene la cantidad y el porcentaje de valores únicos por columna.

        Returns:
            pd.DataFrame: Resumen con la cantidad y porcentaje de valores únicos.
        """

        total_filas = len(self.df)

        resumen_unicos = pd.DataFrame({
            "Columna": self.df.columns,
            "Únicos": self.df.nunique()
        })

        resumen_unicos["% Únicos"] = (
            resumen_unicos["Únicos"] / total_filas * 100
        ).round(1)

        return resumen_unicos
    
    # -------------------------------------------------

    def mostrar_unicos(self) -> None:
        """
        Muestra la cantidad y el porcentaje de valores únicos por columna.
        """

        resumen_unicos = self.obtener_unicos()

        tabla = Table(
            title="Valores únicos",
            show_header=True,
            header_style="bold cyan",
        )

        tabla.add_column("Columna", style="green")
        tabla.add_column("Únicos", justify="right")
        tabla.add_column("% Únicos", justify="right")

        for _, fila in resumen_unicos.iterrows():

            porcentaje = fila["% Únicos"]

            if porcentaje >= 90:
                color = "green"
            elif porcentaje >= 30:
                color = "yellow"
            else:
                color = "red"

            tabla.add_row(
                fila["Columna"],
                str(fila["Únicos"]),
                f"[{color}]{porcentaje:.1f}%[/{color}]",
            )

        console.print(tabla)

    # -------------------------------------------------

    def ejecutar(self) -> None:
        """
        Ejecuta la inspección básica.
        """

        self.mostrar_resumen_general()
        self.mostrar_tipos()
        self.mostrar_nulos()
        self.mostrar_unicos()