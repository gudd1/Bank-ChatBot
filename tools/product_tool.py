from tools.api_client import call_api

def product_tool(category: str) -> dict:
    return call_api("products", {"category": category})
