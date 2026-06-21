from tools.listing_tool import listing_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class ListingAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = listing_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Summarize listing information:\n{data}"
        )
        return self.llm(prompt.format(data=data))
