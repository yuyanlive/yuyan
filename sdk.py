import requests

def get_status(api_url: str, api_key: str):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(f"{api_url}/status", headers=headers)
    return response.json()
