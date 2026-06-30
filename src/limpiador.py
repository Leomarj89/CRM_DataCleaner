from rich.console import Console

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
        console.print()

        return self.df