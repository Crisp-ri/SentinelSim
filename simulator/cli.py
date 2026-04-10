from typing import Annotated
from typer import Option
import typer
import config

app = typer.Typer()

@app.command()
def bruteforce(delay: Annotated[float, typer.Option()] = config.BRUTEFORCE_DELAY, target_ip: Annotated[str, typer.Option()] = config.TARGET_IP, attempts: Annotated[str, typer.Option()] = config.ATTEMPTS):
    pass


