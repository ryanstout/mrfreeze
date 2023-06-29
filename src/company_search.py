from decouple import config
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

import rocketreach


class CompanySearch:
    def __init__(self):
        # setup the rocketreach connection
        self.rocket_api = rocketreach.Gateway(api_key=config("ROCKET_REACH_API_KEY"))


# template = """/
# You are a naming consultant for new companies.
# What is a good name for a company that makes {product}?
# """

# prompt = PromptTemplate.from_template("Find")
# prompt.format(product="colorful socks")

# chat = ChatOpenAI(model_name="gpt-4.0", temperature=0.0)
# messages = [
#     SystemMessage(content="You are an expert sales researcher"),
#     HumanMessage(content="Find "),
# ]
# response = chat(messages)

if __name__ == "__main__":
    cs = CompanySearch()
