from typing import Annotated
import typer
from simulator import config
from simulator.scenarios import  bruteforce as bruteforce_module

app = typer.Typer()

@app.command()
def bruteforce(delay: Annotated[float, typer.Option()] = config.BRUTEFORCE_DELAY, target_ip: Annotated[str, typer.Option()] = config.TARGET_IP, attempts: Annotated[int, typer.Option()] = config.ATTEMPTS):
    bruteforce_module.bruteforce(attempts, delay, target_ip)
    print(f"Brute-force simulation completed with {attempts} attempts, delay of {delay} seconds, targeting IP {target_ip}.")


