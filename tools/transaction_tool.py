from tools.api_client import call_api

def transaction_tool(sender: str, receiver: str, amount: str) -> dict:
    return call_api("transaction", {"from": sender, "to": receiver, "amount": amount})
