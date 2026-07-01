from rich.console import Console
from rich.table import Table

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
        
        console.print()

        return self.df