from tools.realty_tool import realty_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class RealtyAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = realty_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Summarize UCO Realty services:\n{data}"
        )
        return self.llm(prompt.format(data=data))
