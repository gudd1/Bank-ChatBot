from tools.api_client import call_api

def atm_tool() -> dict:
    return call_api("atm-locker")
