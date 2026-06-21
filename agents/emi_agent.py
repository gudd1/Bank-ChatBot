from tools.emi_tool import emi_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class EmiAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self, amount: int, rate: float, tenure: int) -> str:
        data = emi_tool(amount, rate, tenure)
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Explain EMI calculation results clearly:\n{data}"
        )
        return self.llm(prompt.format(data=data))
