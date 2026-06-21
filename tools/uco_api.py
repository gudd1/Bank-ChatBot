import requests


UCO_API_URL = "https://your-uco-bank-api-url.com/loans"


def get_loan_products():

    response = requests.get(
        UCO_API_URL,
        timeout=10
    )

    if response.status_code == 200:
        return response.json()

    return {
        "error": "Unable to fetch loan products"
    }