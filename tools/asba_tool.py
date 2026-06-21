from tools.api_client import call_api

def asba_tool() -> dict:
    return call_api("asba")
