import requests
from .config import API_BASE_URL, ENDPOINTS

def send_event(data):
    response = requests.post(
    url = f"{API_BASE_URL}{ENDPOINTS}",
    json=data,
    timeout=5
)