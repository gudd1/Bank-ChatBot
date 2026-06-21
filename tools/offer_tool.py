from tools.api_client import call_api

def offer_tool() -> dict:
    return call_api("offers")