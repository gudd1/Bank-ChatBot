from tools.api_client import call_api

def auction_tool() -> dict:
    return call_api("property-auction")
