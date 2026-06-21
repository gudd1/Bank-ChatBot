from tools.api_client import call_api

def branch_tool(city: str) -> dict:
    return call_api("branch-search", {"city": city})