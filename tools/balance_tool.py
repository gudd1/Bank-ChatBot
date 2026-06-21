from tools.api_client import call_api

def balance_tool(account_number: str) -> dict:
    return call_api("balance", {"account": account_number})
