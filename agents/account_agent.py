from tools.account_tool import account_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class AccountAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = account_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Summarize account related services:\n{data}"
        )
        return self.llm(prompt.format(data=data))
