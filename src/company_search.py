"""
Simple function for searching for companies on RocketReach.
compaines = search_companies({"keyword": ["Healthcare"]})
"""


import json
from pprint import pprint

import requests
from decouple import config
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage


def search_companies(query: dict, start=1, page_size=10):
    """
    Search for companies on RocketReach by different parameters:
    https://rocketreach.co/api/docs/#operation/searchCompany_create
    """
    url = "https://api.rocketreach.co/api/v2/searchCompany"

    headers = {
        "Api-Key": config("ROCKET_REACH_API_KEY"),
        "Content-Type": "application/json",
    }
    data = {"page_size": page_size, "start": start, "query": query}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # The JSON response from the server
    json_response = response.json()

    return json_response


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
    pass
