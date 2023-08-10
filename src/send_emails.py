import sys
from typing import cast

from gmail_draft_creator import create_draft, send_drafts_from_csv

from src.rocketreach_api import person_lookup

session_id = sys.argv[1]

print(f"Creating drafts for session: {session_id}")

from prisma import Client, Json

prisma = Client()
prisma.connect()


# Load the session from prisma
session = prisma.session.find_unique(where={"id": session_id})

if not session:
    raise Exception(f"Could not find session with id: {session_id}")

# Find all CompanyPerson for the session where readyToSend == true
company_people = prisma.companyperson.find_many(
    where={"sessionId": session.id, "readyToSend": True}
)

for company_person in company_people:
    person = prisma.person.find_unique(where={"id": company_person.personId})
    if person is None:
        print("Could not find person for company person: ", company_person)
        continue

    person_id = cast(int, person.data["id"])

    # test looking up a person
    if person.emailsCache is None or len(person.emailsCache) == 0:
        person_emails = person_lookup(person_id)
        emails = person_emails["emails"]

        # Cache in the Person record
        prisma.person.update(
            where={"id": person.id}, data={"emailsCache": Json(emails)}
        )
    else:
        # Pull from cache
        emails = person.emailsCache

    # Use the first email
    # TODO: could we improve filtering for the best email
    if len(emails) == 0:
        print("No emails found for person: ", person.data["name"])
        continue

    email_address = emails[0]["email"]  # type: ignore
    email_message = company_person.email

    print("To: ", email_address)
    print("Message: ", email_message)

    # Create the draft via the Gmail API
    create_draft(
        email_address,
        email_message,
        template_params={"name": person.name},
        subject="Test subject",
    )
