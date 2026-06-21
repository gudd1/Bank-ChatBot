from tools.api_client import call_api

def realty_tool() -> dict:
    return call_api("uco-realty")
