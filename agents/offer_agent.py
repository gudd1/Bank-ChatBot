from tools.offer_tool import offer_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class OfferAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = offer_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Explain current offers in a friendly way:\n{data}"
        )
        return self.llm(prompt.format(data=data))
