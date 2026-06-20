def balance_tool(account_number: str) -> str:
    # Mock balance lookup
    balances = {"12345": "₹25,000", "67890": "₹12,500"}
    return balances.get(account_number, "Account not found")
