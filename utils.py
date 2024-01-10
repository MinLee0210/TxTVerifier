import requests

def query(payload, url, headers):
    response = requests.post(url, headers=headers, json=payload)
    return response.json()