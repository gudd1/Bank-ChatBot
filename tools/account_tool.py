from tools.api_client import call_api

def account_tool() -> dict:
    return call_api("account-services")
