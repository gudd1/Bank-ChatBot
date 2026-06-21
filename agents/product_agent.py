from tools.product_tool import product_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class ProductAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self, category: str) -> str:
        data = product_tool(category)
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Summarize these banking products for the customer:\n{data}"
        )
        return self.llm(prompt.format(data=data))
