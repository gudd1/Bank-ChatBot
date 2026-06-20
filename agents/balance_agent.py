from tools.balance_tool import balance_tool

class BalanceAgent:
    def run(self, account_number: str) -> str:
        return balance_tool(account_number)