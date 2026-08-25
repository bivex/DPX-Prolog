import os
from pathlib import Path
from typing import List, Optional
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from ..parsers.prolog_parser import RegexPrologParser
from ..detectors.prolog_detector import PrologPatternDetector
from ....application.scan_service import ScanService
from ....domain.pattern import PATTERN_CATALOG

app = typer.Typer(
    name="dpx-prolog",
    help="🦉 Architectural Pattern Detector and Static Analysis Engine for ISO Prolog, SWI-Prolog, CLP(FD/R/Q) & Logic Programming",
    add_completion=False,
)
console = Console()


@app.command(name="scan")
def scan(
    paths: List[Path] = typer.Argument(..., help="Path(s) to Prolog source files or directories to scan"),
    html: Optional[str] = typer.Option(None, "-H", "--html", help="Path to export interactive HTML HUD report"),
    json_path: Optional[str] = typer.Option(None, "-J", "--json", help="Path to export JSON report"),
    markdown: Optional[str] = typer.Option(None, "-M", "--markdown", help="Path to export Markdown report"),
    sarif: Optional[str] = typer.Option(None, "-S", "--sarif", help="Path to export SARIF report"),
):
    """Scan Prolog files for Logic Patterns, CLP Constraints, GoF Patterns, Hazards, and SOLID Principles."""
    parser = RegexPrologParser()
    detector = PrologPatternDetector()
    service = ScanService(parser, detector)

    with console.status("[bold cyan]Scanning Logic Programming codebase...[/bold cyan]"):
        report = service.scan_paths(
            paths=paths,
            html_out=html,
            json_out=json_path,
            markdown_out=markdown,
            sarif_out=sarif,
        )

    table = Table(
        title=f"🦉 DPX-Prolog Findings Summary ({report.total_detections} detected in {report.execution_time_seconds:.4f}s)",
        border_style="cyan",
        header_style="bold cyan",
    )
    table.add_column("#", style="dim", width=4)
    table.add_column("Category", style="magenta")
    table.add_column("Pattern Type", style="bold green")
    table.add_column("Target Functor", style="yellow")
    table.add_column("Confidence", justify="right")
    table.add_column("Location", style="blue")

    for idx, d in enumerate(report.detections, start=1):
        loc_str = f"{os.path.basename(d.location.file_path)}:{d.location.line_number}"
        table.add_row(
            str(idx),
            d.category.value,
            d.pattern_type.value,
            d.target_name,
            f"{d.confidence.percentage}% [{d.confidence.level.value}]",
            loc_str,
        )

    console.print(table)

    if html:
        console.print(f"[bold green]✔[/bold green] Interactive HTML HUD exported to: [bold underline]{html}[/bold underline]")
    if json_path:
        console.print(f"[bold green]✔[/bold green] JSON findings exported to: [bold underline]{json_path}[/bold underline]")
    if markdown:
        console.print(f"[bold green]✔[/bold green] Markdown report exported to: [bold underline]{markdown}[/bold underline]")
    if sarif:
        console.print(f"[bold green]✔[/bold green] SARIF file exported to: [bold underline]{sarif}[/bold underline]")


@app.command(name="catalog")
def catalog():
    """Display catalog of all 45 supported Prolog design patterns, constraints, and declarative hazards."""
    table = Table(
        title="🦉 DPX-Prolog Pattern & Hazard Catalog (45 Rules)",
        border_style="cyan",
        header_style="bold cyan",
    )
    table.add_column("Category", style="magenta")
    table.add_column("Pattern Type", style="bold green")
    table.add_column("Name", style="yellow")
    table.add_column("Default Weight", justify="right")
    table.add_column("Description", style="dim")

    for ptype, meta in PATTERN_CATALOG.items():
        table.add_row(
            meta.category.value,
            ptype.value,
            meta.name,
            f"{int(meta.default_weight * 100)}%",
            meta.description,
        )

    console.print(table)


if __name__ == "__main__":
    app()
