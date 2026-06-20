from tools.transaction_tool import transaction_tool

class TransactionAgent:
    def run(self, sender: str, receiver: str, amount: str) -> str:
        return transaction_tool(sender, receiver, amount)
