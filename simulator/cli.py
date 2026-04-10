from typer import Annotated, Argument
import typer
import config

def bruteforce(delay: Annotated[int, typer.Argument()] = config.BRUTEFORCE_DELAY):
    pass

