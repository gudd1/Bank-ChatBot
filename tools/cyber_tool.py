from tools.api_client import call_api

def cyber_tool() -> dict:
    return call_api("cyber-security-awareness")
