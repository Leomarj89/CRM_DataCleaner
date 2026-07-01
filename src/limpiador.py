from rich.console import Console
from rich.table import Table
import pandas as pd
from unidecode import unidecode

console = Console()


class LimpiadorDatos:
    """
    Limpia y normaliza los datos del DataFrame.

    Esta clase contiene los métodos encargados de preparar la
    información antes de su clasificación y exportación.
    """

    def __init__(
        self,
        dataframe,
        columnas_detectadas,
    ):
        """
        Inicializa el limpiador.

        Args:
            dataframe:
                DataFrame que será limpiado.

            columnas_detectadas:
                Diccionario con las columnas importantes detectadas
                por el Inspector.
        """

        self.df = dataframe
        self.columnas = columnas_detectadas
    
    # -------------------------------------------------
    
    def obtener_columna(self, tipo_columna: str):
        """
        Obtiene una columna del DataFrame utilizando el tipo detectado.

        Args:
            tipo_columna:
                Tipo de columna definido en ALIAS_COLUMNAS.

        Returns:
            pd.Series | None:
                Serie correspondiente o None si la columna no existe.
        """

        nombre_columna = self.columnas.get(tipo_columna)

        if nombre_columna is None:
            return None

        return self.df[nombre_columna]
    
    # -------------------------------------------------

    def actualizar_columna(
    self,
    tipo_columna: str,
    serie: pd.Series,
    ) -> None:
        """
        Actualiza una columna del DataFrame.

        Args:
            tipo_columna:
                Tipo de columna definido en ALIAS_COLUMNAS.

            serie:
                Serie con los datos ya procesados.
        """

        nombre_columna = self.columnas.get(tipo_columna)

        if nombre_columna is None:
            return

        self.df[nombre_columna] = serie
    
    # -------------------------------------------------
    
    def eliminar_espacios(
    self,
    serie: pd.Series
    ) -> pd.Series:
        """
        Elimina espacios al inicio, al final y espacios dobles.

        Args:
            serie:
                Serie de texto a limpiar.

        Returns:
            pd.Series:
                Serie normalizada.
        """

        return (
            serie
            .fillna("")
            .astype(str)
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
        )
    
    # -------------------------------------------------

    def normalizar_texto(
    self,
    serie: pd.Series,
    ) -> pd.Series:
        """
        Normaliza el texto de una serie.

        Convierte el contenido a mayúsculas y elimina acentos.

        Args:
            serie:
                Serie de texto.

        Returns:
            pd.Series:
                Serie normalizada.
        """

        return (
            serie
            .fillna("")
            .astype(str)
            .map(unidecode)
            .str.upper()
        )

    # -------------------------------------------------

    def mostrar_columnas_disponibles(self) -> None:
        """
        Muestra las columnas disponibles para iniciar el proceso de limpieza.
        """

        tabla = Table(
            title="Columnas disponibles para limpieza",
            show_header=True,
            header_style="bold cyan",
        )

        tabla.add_column("Tipo", style="green")
        tabla.add_column("Columna")

        for tipo, columna in self.columnas.items():

            if columna is None:

                tabla.add_row(
                    tipo.capitalize(),
                    "[red]No detectada[/red]",
                )

            else:

                tabla.add_row(
                    tipo.capitalize(),
                    f"[green]{columna}[/green]",
                )

        console.print()
        console.print(tabla)

    # -------------------------------------------------

    def ejecutar(self):
        """
        Ejecuta el proceso de limpieza.

        Returns:
            pd.DataFrame:
                DataFrame limpio.
        """

        console.print()
        console.print(
            "[bold cyan]Iniciando limpieza de datos...[/bold cyan]"
        )

        self.mostrar_columnas_disponibles()

        profesiones = self.obtener_columna("profesion")

        if profesiones is not None:

            profesiones = self.eliminar_espacios(
                profesiones
            )

            profesiones = self.normalizar_texto(
                profesiones
            )

            self.actualizar_columna(
                "profesion",
                profesiones,
            )

        console.print()

        return self.df