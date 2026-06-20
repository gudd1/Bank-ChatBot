def branch_tool(city: str) -> str:
    branches = {
        "Mumbai": "Indian Bank, Fort Branch, Mumbai",
        "Delhi": "Indian Bank, Connaught Place Branch, Delhi",
        "Chennai": "Indian Bank, T. Nagar Branch, Chennai"
    }
    return branches.get(city, "Branch not found in this city")