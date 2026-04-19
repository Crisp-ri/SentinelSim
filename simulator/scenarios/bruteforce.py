import time
from simulator.client import send_event
from simulator import config


def bruteforce(attempts: int, delay: float, target_ip: str):
    for i in range(attempts):
        send_event({
            "source_ip": config.SOURCE_IP,
            "target": target_ip,
            "payload": config.PAYLOAD,
            "port": config.TARGET_PORT
        })
        time.sleep(delay)