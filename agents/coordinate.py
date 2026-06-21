"""from langchain.llms import OpenAI"""
from urllib import response

from langchain_openai import OpenAI
from tools.api_client import call_api
from langchain_core.prompts import PromptTemplate

from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from tools.api_client import call_api
from agents.loan_agent import LoanAgent
# import other agents similarly...
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import json

load_dotenv()  # loads variables from .env
api_key = os.getenv("OPENAI_API_KEY")


class CoordinatorAgent:
    def __init__(self): 
        """self.llm = OpenAI(temperature=0)"""
        """self.llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
        )"""
        self.llm = ChatOllama(
            model="llama3",
            temperature=0
       )
        self.loan_agent = LoanAgent()
        # initialize other agents...
    """def get_loan_answer(self): 
        api_data = self.loan_agent.run( "home loan" ) 
        response = self.llm.invoke( f Convert this bank API response into a customer friendly answer: {api_data}  ) can you make this how exactly it would look like this?"""

    def classify_intent(self, query: str) -> str:
        prompt = PromptTemplate(
            input_variables=["query"],
            template=(
                "Classify the banking intent of this query: {query}. "
                "Options: deposit, loan, digital, offers, whatsnew, branch, asba, "
                "realty, grievance, locker, listing, auction, cyber, atm, account, emi."
            )
        )
        # format the prompt
        formatted_prompt = prompt.format(query=query)
        # invoke the LLM
        response = self.llm.invoke(formatted_prompt)
        # return the text content
        return response.content.strip().lower()
     
    

    """def extract_entities(self, query: str) -> dict:
        prompt = PromptTemplate(
            input_variables=["query"],
            template="Extract structured banking entities from this query: {query}. Return JSON with keys: amount, rate, tenure, city, account_number, loan_type."
        )
        return self.llm(prompt.format(query=query))
        response = self.llm.invoke(
    prompt.format(query=query)
)
        return response.content"""
    def extract_entities(self, query: str):

        prompt = PromptTemplate(
        input_variables=["query"],
        template=(
            "Extract structured banking entities from this query: {query}. "
            "Return ONLY valid JSON. "
            "Keys: amount, rate, tenure, city, account_number, loan_type."
        )
    )

        response = self.llm.invoke(
        prompt.format(query=query)
        )

        print("ENTITY OUTPUT:", response.content)

        try:
           return json.loads(response.content)
        except Exception:
           return {}
 
    def route(self, query: str) -> str:
        intent = self.classify_intent(query).lower()
        entities = self.extract_entities(query)

        if "loan" in intent:
            loan_type = entities.get("loan_type")
            """return self.loan_agent.run(entities.get("loan_type", None))"""
            if not loan_type:
               loan_type = "personal loan"

               return self.loan_agent.run(loan_type)
            loan_type = entities.get("loan_type")

       
          
        
          
        elif "deposit" in intent:
            data = call_api("deposit-products")
        elif "digital" in intent:
            data = call_api("digital-products")
        elif "offers" in intent:
            data = call_api("offers")
        elif "whatsnew" in intent:
            data = call_api("whats-new")
        elif "branch" in intent:
            city = entities.get("city", "Mumbai")
            data = call_api("branch-search", {"city": city})
        elif "emi" in intent:
            amount = entities.get("amount", 500000)
            rate = entities.get("rate", 8.5)
            tenure = entities.get("tenure", 60)
            data = call_api("emi-calculator", {"amount": amount, "rate": rate, "tenure": tenure})
        else:
            return "Sorry, I couldn't understand your request."

        # Summarize API response
        response_prompt = PromptTemplate(
            input_variables=["data"],
            template="Convert this banking API response into a polite, helpful answer:\n{data}"
        )
        response = self.llm.invoke(
    response_prompt.format(data=data)
)
   
        return response.content
        """return self.llm(response_prompt.format(data=data))"""
