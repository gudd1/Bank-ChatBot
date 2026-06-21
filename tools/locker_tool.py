from tools.api_client import call_api

def locker_tool() -> dict:
    return call_api("apply-locker")
