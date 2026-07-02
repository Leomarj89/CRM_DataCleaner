from rich.console import Console
from rich.table import Table
import pandas as pd
from unidecode import unidecode
from config import (
    PATRONES_PROFESION,
    REEMPLAZOS_PROFESION,
)

console = Console()


class LimpiadorDatos:
    """
    Limpia y normaliza los datos del DataFrame.

    Esta clase contiene los métodos encargados de preparar la
    información antes de su clasificación y exportación.
    """

    def __init__(
        self,
        dataframe: pd.DataFrame,
        columnas_detectadas: dict[str, str | None],
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
    
    def obtener_columna(
        self,
        tipo_columna: str,
    ) -> pd.Series | None:
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

    def aplicar_transformaciones(
    self,
    serie: pd.Series,
    transformaciones: list,
    ) -> pd.Series:
        """
        Aplica una secuencia de transformaciones sobre una serie.

        Args:
            serie:
                Serie a transformar.

            transformaciones:
                Lista de funciones de transformación.

        Returns:
            pd.Series:
                Serie transformada.
        """

        for transformacion in transformaciones:

            serie = transformacion(serie)

        return serie
    
    # -------------------------------------------------

    def limpiar_profesiones(self) -> None:
        """
        Limpia y normaliza la columna de profesiones.
        """

        profesiones = self.obtener_columna("profesion")

        if profesiones is None:
            return

        profesiones = self.aplicar_transformaciones(
            profesiones,
            [
                self.eliminar_espacios,
                self.normalizar_texto,
                self.eliminar_puntuacion,
                lambda serie: self.eliminar_patrones(
                    serie,
                    PATRONES_PROFESION,
                ),
                self.eliminar_espacios_multiples,
                lambda serie: self.reemplazar_valores(
                    serie,
                    REEMPLAZOS_PROFESION,
                ),
            ],
        )

        self.actualizar_columna(
            "profesion",
            profesiones,
        )
    
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

    def eliminar_puntuacion(
    self,
    serie: pd.Series,
    ) -> pd.Series:
        """
        Elimina los signos de puntuación más comunes.

        Args:
            serie:
                Serie de texto.

        Returns:
            pd.Series:
                Serie sin signos de puntuación.
        """

        return (
            serie
            .str.replace(".", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.replace(";", "", regex=False)
            .str.replace(":", "", regex=False)
        )
    
    # -------------------------------------------------

    def eliminar_patrones(
    self,
    serie: pd.Series,
    patrones: list[str],
    ) -> pd.Series:
        """
        Elimina una lista de patrones utilizando expresiones regulares.

        Args:
            serie:
                Serie de texto.

            patrones:
                Lista de patrones regex a eliminar.

        Returns:
            pd.Series:
                Serie con los patrones eliminados.
        """

        for patron in patrones:

            serie = serie.str.replace(
                patron,
                "",
                regex=True,
            )

        return serie
    
    # -------------------------------------------------

    def reemplazar_valores(
    self,
    serie: pd.Series,
    reemplazos: dict[str, str],
    ) -> pd.Series:
        """
        Reemplaza valores utilizando un diccionario.

        Args:
            serie:
                Serie de texto.

            reemplazos:
                Diccionario de reemplazos.

        Returns:
            pd.Series:
                Serie con los valores reemplazados.
        """

        return serie.replace(reemplazos)
    
    # -------------------------------------------------

    def eliminar_espacios_multiples(
    self,
    serie: pd.Series,
    ) -> pd.Series:
        """
        Reemplaza múltiples espacios consecutivos por uno solo.

        Args:
            serie:
                Serie de texto.

        Returns:
            pd.Series:
                Serie con espacios normalizados.
        """

        return serie.str.replace(
            r"\s+",
            " ",
            regex=True,
        ).str.strip()

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

    def ejecutar(self) -> pd.DataFrame:
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

        self.limpiar_profesiones()

        console.print()

        return self.df