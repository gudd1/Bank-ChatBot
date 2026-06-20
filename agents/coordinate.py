from agents.balance_agent import BalanceAgent
from agents.loan_agent import LoanAgent
from agents.branch_agent import BranchAgent
from agents.transaction_agent import TransactionAgent



class CoordinatorAgent:
    def __init__(self):
        self.balance_agent = BalanceAgent()
        self.loan_agent = LoanAgent()
        self.branch_agent = BranchAgent()
        self.transaction_agent = TransactionAgent()

    def show_products(self) -> str:
        return (
            "🏦 Welcome to Indian Bank! Here are our product categories:\n"
            "- Deposit Products: Savings Account, Fixed Deposit, Recurring Deposit\n"
            "- Loan Products: Home Loan, Car Loan, Personal Loan, Education Loan\n"
            "- Digital Products: NetBanking, Mobile Banking, UPI, Debit/Credit Cards\n"
            "Please type which category you'd like to explore."
        )

    def route(self, query: str) -> str:
        query_lower = query.lower()

        # Product categories
        if "deposit" in query_lower:
            return "Deposit Products: Savings Account, Fixed Deposit, Recurring Deposit."
        elif "loan" in query_lower:
            return "Loan Products: Home Loan, Car Loan, Personal Loan, Education Loan."
        elif "digital" in query_lower or "online" in query_lower:
            return "Digital Products: NetBanking, Mobile Banking, UPI, Debit/Credit Cards."
        elif "products" in query_lower or "options" in query_lower:
            return self.show_products()

        # Banking services
        elif "balance" in query_lower:
            return self.balance_agent.run("12345")  # Example account
        elif "branch" in query_lower or "atm" in query_lower:
            return self.branch_agent.run("Mumbai")  # Example city
        elif "transfer" in query_lower or "transaction" in query_lower:
            return self.transaction_agent.run("12345", "67890", "₹5000")  # Example transfer

        else:
            return "Sorry, I couldn't understand your request. Try asking about products, balance, loans, or transactions."
