from pprint import pprint

import openapi_client
from decouple import config
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from openapi_client.apis.tags import company_profiles_api
from openapi_client.model.api_public_company_search_input import (
    APIPublicCompanySearchInput,
)
from openapi_client.model.company_query import CompanyQuery


class CompanySearch:
    def __init__(self):
        # setup the rocketreach connection
        # self.rocket_api = rocketreach.Gateway(api_key=config("ROCKET_REACH_API_KEY"))

        # import code

        # code.interact(local=locals())

        # See configuration.py for a list of all supported configuration parameters.
        configuration = openapi_client.Configuration(
            host="https://rocketreach.co/api/v2"
        )

        # The client must configure the authentication and authorization parameters
        # in accordance with the API server security policy.
        # Examples for each auth method are provided below, use the example that
        # satisfies your auth use case.

        # Configure API key authorization: RocketReach API Key
        configuration.api_key["RocketReach API Key"] = config("ROCKET_REACH_API_KEY")
        import code

        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = company_profiles_api.CompanyProfilesApi(api_client)

            # example passing only required values which don't have defaults set
            body = APIPublicCompanySearchInput(
                start=1,
                page_size=1,
                query=CompanyQuery(keyword=("Healthcare")),
                # order_by="relevance",
            )
            print(body)
            code.interact(local=locals())
            try:
                # Search Companies
                print("HERE")
                api_response = api_instance.search_company_create(
                    body=body,
                )
                print("FAILS")

                code.interact(local=locals())

            except openapi_client.ApiException as e:
                print(
                    "Exception when calling CompanyProfilesApi->search_company_create: %s\n"
                    % e
                )
            print("1")
            # drop into python repl


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
