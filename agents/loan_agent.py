from tools.loan_tool import loan_tool

class LoanAgent:
    def run(self, query: str) -> str:
        return loan_tool(query)