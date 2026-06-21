from tools.asba_tool import asba_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class AsbaAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = asba_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Explain ASBA services clearly:\n{data}"
        )
        return self.llm(prompt.format(data=data))
