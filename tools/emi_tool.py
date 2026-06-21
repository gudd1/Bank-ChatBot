from tools.api_client import call_api

def emi_tool(amount: int, rate: float, tenure: int) -> dict:
    return call_api("emi-calculator", {"amount": amount, "rate": rate, "tenure": tenure})
