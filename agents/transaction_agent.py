from tools.transaction_tool import transaction_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class TransactionAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self, sender: str, receiver: str, amount: str) -> str:
        data = transaction_tool(sender, receiver, amount)
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Explain this transaction result politely:\n{data}"
        )
        return self.llm(prompt.format(data=data))
