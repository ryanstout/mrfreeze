import random

import requests
from langchain import LLMChain
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import BaseOutputParser
from langchain.text_splitter import CharacterTextSplitter


def shuffle(l: list) -> list:
    return random.sample(l, len(l))


class MapCleanupParser(BaseOutputParser[str]):
    """Clean up and scores that come out of the map step"""

    @property
    def _type(self) -> str:
        return "str"

    def parse(self, text: str) -> str:
        """Parse the output, removing any rankings"""

        # Strip off anything after a colon or a " - " on each line
        text = "\n".join(
            [
                line.split(":")[0].split(" - ")[0]
                for line in text.split("\n")
                if line.strip()
            ]
        )

        # Remove any tripple backticks
        text = text.replace("```", "")

        # remove blank lines
        text = "\n".join([line for line in text.split("\n") if line.strip()])

        # print count of lines
        print(f"Got {len(text.splitlines())} matching titles")

        return text


job_query = "hiring database administrators"
limit = 100

llm = ChatOpenAI(
    temperature=0.0, model="gpt-4", verbose=False, max_retries=2, request_timeout=6000
)
token_window_size = 8_000

url = "https://static.rocketreach.co/job-titles/normalized_titles_display_names.txt"
titles = requests.get(url).text

# Split the titles on \n, shuffle, then truncate to the first 1000, then join back to a string
# titles = "\n".join(random.sample(titles.split("\n"), 1000))

# Shuffle titles so we don't get too many relates jobs in a chunk
titles = "\n".join(shuffle(titles.split("\n")))

# Limit to 3k job titles for testing
titles = "\n".join(shuffle(titles.split("\n")[:5000]))


map_prompt = HumanMessagePromptTemplate.from_template(
    "Given the following list of job titles, assign each job title a score from 0 to 100 based on how likely the job would be to be in charge of {job_query}. Only return jobs with a score of over 95.\n\n```{titles}```"
)


reduce_prompt = HumanMessagePromptTemplate.from_template(
    "Rank the following job titles based on how likely the job described would be to be in charge of {job_query}. Return the top {limit} results separated by new lines, do not include numbers.\n\n```{titles}```"
)

map_prompt = ChatPromptTemplate.from_messages([map_prompt])
reduce_prompt = ChatPromptTemplate.from_messages([reduce_prompt])

map_llm_chain = LLMChain(
    llm=llm, prompt=map_prompt, output_parser=MapCleanupParser(), verbose=False
)

reduce_llm_chain = LLMChain(llm=llm, prompt=reduce_prompt)

# Once we have a set of mapped documents, stuff them into a single prompt and reduce
reduce_chain = StuffDocumentsChain(
    llm_chain=reduce_llm_chain,
    document_variable_name="titles",
)

combine_documents = MapReduceDocumentsChain(
    llm_chain=map_llm_chain,
    reduce_documents_chain=reduce_chain,
    document_variable_name="titles",
    return_intermediate_steps=False,
    verbose=False,
)

len_func = llm.get_num_tokens

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=(token_window_size // 2) - 1000,
    chunk_overlap=0,
    length_function=len_func,
    add_start_index=False,
)

title_documents = text_splitter.create_documents(texts=[titles])
results = combine_documents.run(
    input_documents=title_documents,
    job_query=job_query,
    limit=limit,
)

import code

code.interact(local=locals())
