from tools.whatsnew_tool import whatsnew_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class WhatsNewAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = whatsnew_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Summarize what's new at the bank:\n{data}"
        )
        return self.llm(prompt.format(data=data))
