"""
Takes in a query and ranks the list of rocketreach normalized titles based on how likely the title is to match the query.
Example: <rank the following list of job titles based on how likely the job described would be responsible for> purchasing software products.
"""
import os
import pickle
import random
import time

import langchain
import requests
from decouple import config
from langchain import LlamaCpp, LLMChain, PromptTemplate
from langchain.callbacks import get_openai_callback
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.mapreduce import MapReduceChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.text_splitter import CharacterTextSplitter

from src.batteries import memoize_to_disk, shuffle

langchain.debug = True


# llm = OpenAI(temperature=0.0)
# llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")
# token_window_size = 4096


# llm = ChatOpenAI(
#     temperature=0.0,
#     model="gpt-3.5-turbo-16k",
#     max_retries=0,
#     verbose=True,
# )
# token_window_size = 16_000


llm = ChatOpenAI(
    temperature=0.0, model="gpt-4", verbose=True, max_retries=0, request_timeout=6000
)
token_window_size = 8_000

# n_gpu_layers = 40  # Change this value based on your model and your GPU VRAM pool.
# n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.

# llm = LlamaCpp(
#     model_path="./models/ggml-alpaca-7b-q4.bin",
#     n_gpu_layers=n_gpu_layers,
#     n_batch=n_batch,
#     n_ctx=8192,
#     # callback_manager=callback_manager,
#     verbose=True,
#     # use_mlock=True,
#     # verbose=False,
# )

# llm = LlamaCpp(
#     model_path="./models/stable-vicuna-13B.ggmlv3.q4_K_M.bin",
#     n_gpu_layers=40,
#     seed=random.randint(1, 2**31),
# )

print("Model loaded")


@memoize_to_disk
def rocketreach_title_search_rank(
    job_query: str, limit: int = 100, map_limit: int = 100
) -> list[str]:
    with get_openai_callback() as cb:
        # Pull in the list of normalized titles from the provided url
        url = "https://static.rocketreach.co/job-titles/normalized_titles_display_names.txt"
        titles = requests.get(url).text

        # Split the titles on \n, shuffle, then truncate to the first 1000, then join back to a string
        # titles = "\n".join(random.sample(titles.split("\n"), 1000))

        # Shuffle titles so we don't get too many relates jobs in a chunk
        titles = "\n".join(shuffle(titles.split("\n")))

        # print(titles)

        # map_prompt = PromptTemplate(
        #     input_variables=["job_query", "titles", "map_limit"],
        #     template="Rank the following job titles based on how likely the job described would be to be in charge of {job_query}. Return the top {map_limit} results separated by new lines, do not include numbers.\n\n```{titles}```",
        # )

        # reduce_prompt = PromptTemplate(
        #     input_variables=["job_query", "titles", "limit"],
        #     template="Rank the following job titles based on how likely the job described would be to be in charge of {job_query}. Return the top {limit} results separated by new lines, do not include numbers.\n\n```{titles}```",
        # )

        use_langchain = False
        disable_parallel = True

        map_prompt = HumanMessagePromptTemplate.from_template(
            # "Rank the following job titles based on how likely the job described would be to be in charge of {job_query}. Return the top {map_limit} results separated by new lines, do not include numbers.\n\n```{titles}```"
            "Given the following list of job titles, assign each job title a score from 0 to 100 based on how likely the job would be to be in charge of {job_query}. Only return jobs with a score of over 95.\n\n```{titles}```"
        )
        reduce_prompt = HumanMessagePromptTemplate.from_template(
            "Rank the following job titles based on how likely the job described would be to be in charge of {job_query}. Return the top {limit} results separated by new lines, do not include numbers.\n\n```{titles}```"
        )

        map_prompt = ChatPromptTemplate.from_messages([map_prompt])
        reduce_prompt = ChatPromptTemplate.from_messages([reduce_prompt])

        map_llm_chain = LLMChain(llm=llm, prompt=map_prompt, verbose=True)

        # result = map_llm_chain.run(
        #     job_query=job_query, titles=titles, map_limit=map_limit
        # )

        # print("RESULT", result)
        # # drop into repl
        # import code

        # code.interact(local=locals())

        reduce_llm_chain = LLMChain(llm=llm, prompt=reduce_prompt)

        generative_result_reduce_chain = StuffDocumentsChain(
            llm_chain=reduce_llm_chain,
            document_variable_name="titles",
        )

        combine_documents = MapReduceDocumentsChain(
            llm_chain=map_llm_chain,
            # combine_document_chain=generative_result_reduce_chain,
            reduce_documents_chain=generative_result_reduce_chain,
            document_variable_name="titles",
            return_intermediate_steps=False,
            verbose=True,
        )

        len_func = llm.get_num_tokens

        # def num_tokens(x):
        #     token_count = llm.get_num_tokens(x)
        #     print("TOKEN COUNT: ", token_count)
        #     return token_count

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=(token_window_size // 2) - 1000,
            chunk_overlap=0,
            length_function=len_func,
            add_start_index=False,
        )

        title_documents = text_splitter.create_documents(texts=[titles])

        if not use_langchain or disable_parallel:
            import openai

            openai.api_key = os.getenv("OPENAI_API_KEY")

            results = []
            for title_document in title_documents:
                prompt = map_prompt.format(
                    job_query=job_query,
                    titles=title_document.page_content,
                    # map_limit=map_limit,
                )

                print("Run prompt")
                t1 = time.time()
                map_results = openai.ChatCompletion.create(
                    model="gpt-4", messages=[{"role": "user", "content": prompt}]
                )
                t2 = time.time()

                result = map_results.choices[0].message.content

                # Strip off anything after a colon or a " - " on each line
                result = "\n".join(
                    [
                        line.split(":")[0].split(" - ")[0]
                        for line in result.split("\n")
                        if line.strip()
                    ]
                )

                # Remove any tripple backticks
                result = result.replace("```", "")

                # remove blank lines
                result = "\n".join(
                    [line for line in result.split("\n") if line.strip()]
                )

                print("RESULT IN: ", t2 - t1, len(result.split("\n")))
                results.append(result)

                # print("NOW WITH LANGCHAIN")
                # t1 = time.time()
                # # Run document through the map chain
                # map_results = map_llm_chain.run(
                #     job_query=job_query,
                #     titles=title_document.page_content,
                #     map_limit=map_limit,
                # )
                # t2 = time.time()
                # print("LANGCHAIN RAN IN ", t2 - t1)

            # results = reduce_llm_chain.run(
            #     job_query=job_query, titles="\n".join(results), limit=limit
            # )

            print(f"----------------\n{results}\n\n")
            prompt = reduce_prompt.format(
                job_query=job_query, titles="\n".join(results), limit=limit
            )

            print(
                "Final Prompt",
                prompt,
                "\n\nPrompt Length: ",
                len(prompt),
                "Prompt Lines: ",
                len(prompt.split("\n")),
            )
            results = openai.ChatCompletion.create(
                model="gpt-4", messages=[{"role": "user", "content": prompt}]
            )
            results = results.choices[0].message.content
            print("FINAL RESULTS: ", results)
            import code

            code.interact(local=locals())

        # results = combine_documents.run(
        #     input_documents=title_documents,
        #     job_query=job_query,
        #     map_limit=map_limit,
        #     limit=limit,
        # )

        # import code

        # code.interact(local=locals())

        # split results on newline and remove any empty string values
        results = [x for x in results.split("\n") if x != ""]

        # Remove any titles that are not in the original list of titles and print an error for any titles that were
        # removed
        removed_titles = []
        for title in results:
            if title not in titles:
                removed_titles.append(title)
                results.remove(title)

        if len(removed_titles) > 0:
            print(
                f"Removed {len(removed_titles)} titles that were not in the original list of titles: {removed_titles}"
            )
            print(removed_titles)

        if len(results) == 0:
            raise Exception("No job titles were returned")

        return results

    # chain = LLMChain(llm=llm, prompt=prompt)

    # result = chain.run({"job_query": query})


if __name__ == "__main__":
    r = rocketreach_title_search_rank("purchasing software")

    import code

    code.interact(local=locals())
