from tools.grievance_tool import grievance_tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class GrievanceAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run(self) -> str:
        data = grievance_tool()
        prompt = PromptTemplate(
            input_variables=["data"],
            template="Explain grievance portal usage:\n{data}"
        )
        return self.llm(prompt.format(data=data))
