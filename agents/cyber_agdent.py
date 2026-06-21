from tools.cyber_tool import cyber_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class CyberAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = cyber_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Explain cyber security awareness tips:\n{data}"
        )
        return self.llm(prompt.format(data=data))
