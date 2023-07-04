# Create or resume a session

import code

from src.rocketreach_api import search_companies, search_people
from src.rocketreach_title_search_ranker import rocketreach_title_search_rank
from src.sessions import Session

# Create or resume a session, gets the name of the session, company targeting
# query, and employee title targeting query
session = Session.create_or_resume()

job_titles = rocketreach_title_search_rank("purchasing software", limit=50)
print("Finding people with the following job titles: ", job_titles)

compaines = search_companies({"keyword": ["Healthcare"]})


company_employees = {}

for company in compaines["companies"]:
    print(">>>> COMPANY: ", company["name"])
    employees = company_employees[company["name"]] = []

    for job_title in job_titles:
        print(">>>>>> JOB TITLE: ", job_title)

        # Search for people with each job title in order, then when we get enough people, stop searching
        people = search_people(
            {"company_id": [company["id"]], "normalized_title": job_titles}
        )
        code.interact(local=locals())

        for person in people["profiles"]:
            print(person["name"], person["current_title"], person["normalized_title"])
