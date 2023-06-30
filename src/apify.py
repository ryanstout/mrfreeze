import os

os.environ["LANGCHAIN_TRACING"] = "true"

import json
from pprint import pprint
from typing import List

import langchain
from decouple import config
from langchain.document_loaders.base import Document
from langchain.indexes import VectorstoreIndexCreator
from langchain.output_parsers import PydanticOutputParser
from langchain.utilities import ApifyWrapper
from pydantic import BaseModel, Field, validator

langchain.debug = True


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["APIFY_API_TOKEN"] = config("APIFY_API_KEY")


class TeamMember(BaseModel):
    name: str = Field(description="the team members name")
    title: str = Field(description="the team members title")
    bio: str = Field(
        description="the team members bio or any other text associated with the team member"
    )


class TeamMembers(BaseModel):
    members: List[TeamMember] = Field(description="a list of team members")


parser = PydanticOutputParser(pydantic_object=TeamMembers)

# print(parser.get_format_instructions())


apify = ApifyWrapper()

print("Setup crawler")
loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={
        "startUrls": [
            {"url": "https://www.nextfrontiercapital.com/team"},
            {"url": "https://www.nextfrontiercapital.com/"},
        ],
        "maxCrawlPages": 10,
        "crawlerType": "cheerio",
    },
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
)

print("Vector index")
index = VectorstoreIndexCreator().from_loaders([loader])

print("Query")
# query = """Give me a list of all team members. Return it in the following format

# [
#     {
#         "name": "John Doe",
#         "title": "CEO",
#         "bio": "John Doe is the CEO of Some Venture Fund"
#     }
# ]
# """

query = """Give me a list of all team members you can find. Return the name and title of each team member."""

# Return it in the following format:

# ```
# [
#     {
#         "name": "John Doe",
#         "title": "CEO",
#         "bio": "John is the CEO of Some Venture Fund. He spent the past 20 years building amazing companies. He served on the board of Intel from 1999 to 2020."
#     }
# ]`
# ```
# """

result = index.query_with_sources(query)

answer = result["answer"]
print("ANSWER: ", answer)

# answer = parser.parse(result["answer"])

# print("Parsed ANSWER: ", answer)

# import code

# code.interact(local=locals())
