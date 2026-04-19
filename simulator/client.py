import requests
from .config import API_BASE_URL, ENDPOINT

def send_event(data):
    response = requests.post(
    url = f"{API_BASE_URL}{ENDPOINT}",
    json=data,
    timeout=5
)