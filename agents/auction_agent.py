from tools.auction_tool import auction_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class AuctionAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = auction_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Explain auctioning of properties:\n{data}"
        )
        return self.llm(prompt.format(data=data))
