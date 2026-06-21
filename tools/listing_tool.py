from tools.api_client import call_api

def listing_tool() -> dict:
    return call_api("listing")
