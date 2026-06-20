from agents.coordinate import CoordinatorAgent


def chat():
    coordinator = CoordinatorAgent()
    print("🏦 Indian Bank Chatbot Ready! Type 'exit' to quit.\n")
    print("Please choose a category to explore:")
    print("1. Deposit Products")
    print("2. Loan Products")
    print("3. Digital Products")
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
        else:
            response = coordinator.route(user_input)

        print(f"Bot: {response}")



if __name__ == "__main__":
    chat()
