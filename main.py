from agents.coordinate import CoordinatorAgent
from tools.api_client import call_api
from tools.api_client import call_api
def chat():
    coordinator = CoordinatorAgent()
    print("🏦 Indian Bank Chatbot Ready! Type 'exit' to quit.\n")
    print("Please choose a category to explore:")
    print("1. Deposit Products")
    print("2. Loan Products")
    print("3. Digital Products")
    print("4. Offers")
    print("5. What's New")
    print("6. Search Branch/IFSC")
    print("7. ASBA")
    print("8. UCO Realty")
    print("9. Online Grievance Portal")
    print("10. Apply for Locker")
    print("11. Listing")
    print("12. Auctioning of Properties")
    print("13. Cyber Security Awareness")
    print("14. ATM Locker")
    print("15. Account Related Services")
    print("16. EMI Calculator")
    print("Or type your own query (e.g., 'Show my balance').\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Handle numeric menu choices
        if user_input == "1":
            response = coordinator.route("deposit products")
        elif user_input == "2":
            response = coordinator.route("loan products")
        elif user_input == "3":
            response = coordinator.route("digital products")
        elif user_input == "4":
            response = coordinator.route("offers")
        elif user_input == "5":
            response = coordinator.route("what's new")
        elif user_input == "6":
            response = coordinator.route("branch ifsc search")
        elif user_input == "7":
            response = coordinator.route("asba")
        elif user_input == "8":
            response = coordinator.route("uco realty")
        elif user_input == "9":
            response = coordinator.route("online grievance portal")
        elif user_input == "10":
            response = coordinator.route("apply for locker")
        elif user_input == "11":
            response = coordinator.route("listing")
        elif user_input == "12":
            response = coordinator.route("auctioning of properties")
        elif user_input == "13":
            response = coordinator.route("cyber security awareness")
        elif user_input == "14":
            response = coordinator.route("atm locker")
        elif user_input == "15":
            response = coordinator.route("account related services")
        elif user_input == "16":
            response = coordinator.route("emi calculator")
        else:
            response = coordinator.route(user_input)

        print(f"Bot: {response}")



if __name__ == "__main__":
    chat()
