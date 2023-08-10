"""
Function for searching for companies on RocketReach.
"""


import json
from pprint import pprint

import requests
from decouple import config
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage


def person_lookup(person_id: int):
    """
    Search for companies on RocketReach by different parameters:
    https://rocketreach.co/api/docs/#operation/person_lookup_read
    """
    url = "https://api.rocketreach.co/api/v2/person/lookup"

    headers = {
        "Api-Key": config("ROCKET_REACH_API_KEY"),
        "Content-Type": "application/json",
    }
    data = {"id": person_id}

    response = requests.get(url, headers=headers, data=json.dumps(data))

    # The JSON response from the server
    json_response = response.json()

    return json_response


def search_people(query: dict, start=1, page_size=10):
    """
    Search for companies on RocketReach by different parameters:
    https://rocketreach.co/api/docs/#operation/searchCompany_create
    """
    url = "https://api.rocketreach.co/api/v2/search"

    headers = {
        "Api-Key": config("ROCKET_REACH_API_KEY"),
        "Content-Type": "application/json",
    }
    data = {"page_size": page_size, "start": start, "query": query}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # The JSON response from the server
    json_response = response.json()

    return json_response


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


if __name__ == "__main__":
    compaines = search_companies({"keyword": ["Healthcare"]}, page_size=2)

    for company in compaines["companies"]:
        print("Company: ", company)
        people = search_people({"company_id": [company["id"]]})
        print("People: ", people)
        for person in people["profiles"]:
            print(person)

    # print(compaines)


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
    compaines = search_companies({"keyword": ["Healthcare"]})

    for company in compaines["companies"]:
        people = search_people({"company_id": company["company_id"]})

        # for person in people["people"]:
        #     print(person["name"]
