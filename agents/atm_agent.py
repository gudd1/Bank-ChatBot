from tools.atm_tool import atm_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class AtmAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = atm_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Explain ATM locker services:\n{data}"
        )
        return self.llm(prompt.format(data=data))
