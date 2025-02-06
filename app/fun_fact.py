# app/fun_fact.py

import requests

def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}/math"
    try:
        response = requests.get(url)
        return response.text if response.status_code == 200 else "No fun fact available."
    except Exception:
        return "Could not fetch fun fact."
