import sys

from prisma import Json

from src import db
from src.rocketreach_api import search_companies, search_people
from src.rocketreach_title_search_ranker import rocketreach_title_search_rank

db_connection = db.application_database_connection()


session_id = sys.argv[1]
keyword = sys.argv[2]
job_description = sys.argv[3]
max_companies = int(sys.argv[4])
max_people_per_company = int(sys.argv[5])


print(
    "************************************\nStarting creation of new session on session id: ",
    session_id,
    "\n> search for companies matching: ",
    keyword,
    "\n> for jobs that: ",
    job_description,
    "\n> max companies: ",
    max_companies,
    "\n> max people per company: ",
    max_people_per_company,
    "\n************************************",
)


def find_or_create_company(company):
    company_id = company["id"]
    # Find the company in the database by rocketreachId
    company_record = db_connection.company.find_first(
        where={"rocketreachId": company_id}
    )

    if not company_record:
        # Save the company
        company_record = db_connection.company.create(
            data={
                "rocketreachId": company_id,
                "name": company["name"],
                "data": Json(company),
            }
        )

    return company_record


def create_session_company(company_id, session_id):
    # Check if the relation already exists
    session_company = db_connection.sessioncompany.find_first(
        where={"sessionId": session_id, "companyId": company_id}
    )

    if not session_company:
        # Save SessionCompany to link session and company
        print("Create session company: ", company_id, session_id)
        db_connection.sessioncompany.create(
            data={
                "sessionId": session_id,
                "companyId": company_id,
            }
        )


def find_or_create_person(person):
    # Find the person in the database by rocketreachId
    person_record = db_connection.person.find_first(
        where={"rocketreachId": person["id"]}
    )

    if not person_record:
        # Save the person
        person_record = db_connection.person.create(
            data={
                "rocketreachId": person["id"],
                "name": person["name"],
                "data": Json(person),
            }
        )

    return person_record


def create_session_person(person_id, session_id):
    # Check if the relation already exists
    session_person = db_connection.sessionperson.find_first(
        where={"sessionId": session_id, "personId": person_id}
    )

    if not session_person:
        # Save SessionPerson to link session and person
        db_connection.sessionperson.create(
            data={
                "sessionId": session_id,
                "personId": person_id,
            }
        )


def create_company_person(company_id, person_id, session_id):
    # Check if the relation exists
    company_person = db_connection.companyperson.find_first(
        where={"companyId": company_id, "personId": person_id}
    )

    if not company_person:
        # Save CompanyPerson to link company and person
        db_connection.companyperson.create(
            data={
                "companyId": company_id,
                "personId": person_id,
                "sessionId": session_id,
            }
        )


job_titles = rocketreach_title_search_rank(job_description)  # , limit=50)
print("Finding people with the following job titles: ", job_titles)

compaines = search_companies({"keyword": [keyword]})

company_employees = {}

company_count = 0

if "companies" not in compaines:
    print("No companies found for keyword: ", keyword, compaines)
    sys.exit(1)


print("Companies: ", compaines)
print("Search returned ", len(compaines["companies"]), " companies")

for company in compaines["companies"]:
    if company_count > max_companies:
        break
    company_count += 1

    company_id = company["id"]
    company_record = find_or_create_company(company)
    create_session_company(company_record.id, session_id)

    print(">>>> COMPANY: ", company["name"])
    employees = company_employees[company["name"]] = []

    for job_title in job_titles:
        print(">>>>>> JOB TITLE: ", job_title)

        # Search for people with each job title in order, then when we get enough people, stop searching
        company_people_count = db_connection.companyperson.count(
            where={"companyId": company_record.id}
        )

        if company_people_count > max_people_per_company:
            break

        # There's no way to sort by a specific field, so we have to query by normalized title one at a time.
        # TODO: we could probably query and split out after, but we don't have any way to know if we got the
        # normalized_titles we wanted first if we hit the limit.
        people = search_people(
            {"company_id": [company["id"]], "normalized_title": [job_title]}
        )

        if "profiles" not in people:
            print("No profiles found for company: ", company["name"], people)
        else:
            for person in people["profiles"]:
                print(
                    person["name"], person["current_title"], person["normalized_title"]
                )

                # Create person and associations
                person_record = find_or_create_person(person)
                create_session_person(person_record.id, session_id)
                create_company_person(company_record.id, person_record.id, session_id)
