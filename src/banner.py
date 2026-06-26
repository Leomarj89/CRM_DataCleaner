from rich.console import Console
from rich.panel import Panel

from config import (
    NOMBRE_PROYECTO,
    VERSION
)

console = Console()


def mostrar_banner():

    console.print()

    console.print(
        Panel.fit(
            f"""
[bold cyan]{NOMBRE_PROYECTO}[/]

Versión {VERSION}

HubSpot • Excel • CSV • CRM
""",
            border_style="cyan",
        )
    )