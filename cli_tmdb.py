#!/usr/bin/env python3
import typer
from utils.commands import cli_tmdb

app = typer.Typer()

app.add_typer(cli_tmdb, name="")

if "__main__" == __name__:
    app()