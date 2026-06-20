def loan_tool(query: str) -> str:
    loans = {
        "home": "Home Loan interest rate: 8.5% per annum",
        "car": "Car Loan interest rate: 9.2% per annum",
        "personal": "Personal Loan interest rate: 11% per annum"
    }
    return loans.get(query.lower(), "Loan type not recognized")