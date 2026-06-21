import requests
import os
BASE_URL = "https://api.ucobank.com/v1"  # Replace with actual UCO Bank API base

def call_api(endpoint: str, params: dict = None) -> dict:
    headers = {"Authorization": f"Bearer {os.getenv('UCO_API_KEY')}"}
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}", params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}