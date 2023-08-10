// Utilities for working with people on the front-end

import type { CompanyPerson, Person, Session } from "@prisma/client"

export class FullPerson {
    constructor(
        public id: string,
        public name: string,
        public selected: boolean,
        public current_title: string,
        public normalized_title: string,
        public linkedin_url: string,
        public email: string
    ) {}
}

export async function savePeople(
    session: Session,
    peopleRecords: FullPerson[],
    selectedPeople: FullPerson[],
    nextPage: () => void
) {
    // write in the selected state to peopleRecords by looking if it is included in selectedPeople
    const updatedPeopleRecords = peopleRecords.map((person) => {
        return {
            ...person,
            // selected if the person object is included in the selectedPeople array
            selected: selectedPeople.map((e) => e.id).includes(person.id),
        }
    })

    // from updatedPeopleRecords, just extract selected state and email value
    const selectedAndEmail = updatedPeopleRecords.map((person) => {
        return {
            id: person.id,
            selected: person.selected,
            email: person.email,
        }
    })

    // Save the data to the remix action
    await fetch(`/sessions/${session.id}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(selectedAndEmail),
    })

    nextPage()
}
export function transformPeople(
    people: (CompanyPerson & { person: Person })[]
) {
    let peopleRecords: FullPerson[]
    if (people) {
        peopleRecords = people.map((companyPerson) => {
            const data = companyPerson.person.data
            if (!data) {
                throw new Error(
                    `Data for companyPerson not found ${companyPerson}`
                )
            }

            return new FullPerson(
                companyPerson.id,
                companyPerson.person.name,
                companyPerson.selected,
                data.current_title,
                data.normalized_title,
                data.linkedin_url,
                companyPerson.email || ""
            )
        })
    } else {
        peopleRecords = []
    }
    return peopleRecords
}
