import pathlib

import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .bin_packer import Bin, BinPacker
from .parser import parse


def pretty_print(bin: Bin):
    text = Text()
    text.append("[ ", style="yellow")
    text.append(
        Text.from_markup("[yellow] | [/]".join(map(str, bin.items)), style="bold")
    )
    if bin.capacity > 0:
        text.append(" | ", style="yellow")
        text.append(str(bin.capacity), style="black")
    text.append(" ]", style="yellow")
    text.append("\n")
    return text


def main(manifest: pathlib.Path):
    project = parse(manifest)
    console = Console()
    console.print(
        Text.from_markup(
            f"Planning [yellow]{project.name}[/yellow] Cuts", style="bold cyan"
        )
    )
    for component in project.components:
        packer = BinPacker[float](component.length, padding=component.kerf)
        p_text = Text()
        boards = packer.pack(component.segments)
        for board in boards:
            p_text.append(pretty_print(board))
        p_text.append(Text.from_markup(f"[bold cyan]{len(boards)}[/] needed"))
        p = Panel(p_text, expand=False, title=Text.from_markup(
            f"Slicing [green]{component.name}[/green]", style="bold cyan"
        ), title_align="left")
        console.print(p)


if __name__ == "__main__":
    typer.run(main)


# TODO: support mitre cuts
