from tools.api_client import call_api

def grievance_tool() -> dict:
    return call_api("grievance-portal")
