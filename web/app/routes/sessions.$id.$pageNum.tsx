import {
    Button,
    Group,
    Pagination,
    Space,
    Stack,
    Textarea,
} from "@mantine/core"
import { useLoaderData, useNavigate, useParams } from "@remix-run/react"
import { DataTable } from "mantine-datatable"
import { useEffect, useRef, useState } from "react"
import { z } from "zod"
import { zx } from "zodix"
import { prisma } from "~/db.server"

class Person {
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

const perPage = 10

export async function action({ request, params }: LoaderArgs) {
    const { id } = zx.parseParams(params, { id: z.string() })

    // Get the JSON passed in
    const companyPeople = JSON.parse(await request.text())

    // update the companyPerson data
    for await (const companyPerson of companyPeople) {
        await prisma.companyPerson.update({
            where: { id: companyPerson.id },
            data: {
                email: companyPerson.email,
                selected: companyPerson.selected,
            },
        })
    }

    return null
}

export async function loader({ params }: LoaderArgs) {
    const { id, pageNum } = zx.parseParams(params, {
        id: z.string(),
        pageNum: zx.NumAsString.optional(),
    })

    const session = await prisma.session.findFirst({
        where: { id: id },
    })

    if (!session) {
        throw new Error("Session not found")
    }

    // Fetch the first company
    const company = await prisma.sessionCompany.findFirst({
        where: { sessionId: session.id },
        include: {
            company: true,
        },
    })

    if (!company) {
        throw new Error("Company not found")
    }

    // Get the CompanyPerson for the company that match this session
    const people = await prisma.companyPerson.findMany({
        where: {
            sessionId: session.id,
            companyId: company.companyId,
        },
        include: { person: true },
        // limit/offset by pageNum and perPage
        take: perPage,
        skip: pageNum ? (pageNum - 1) * perPage : 0,
        orderBy: { id: "desc" },
    })

    const totalPeople = await prisma.companyPerson.count({
        where: {
            sessionId: session.id,
            companyId: company.companyId,
        },
    })

    return { session, company, people, totalPeople }
}

function savePeople(
    session,
    peopleRecords: Person[],
    selectedPeople: Person[]
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
    fetch(`/sessions/${session.id}/0`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(selectedAndEmail),
    })
}

export default function SessionIndex() {
    const { session, company, people, totalPeople } =
        useLoaderData<typeof loader>()

    const [selectedPeople, setSelectedPeople] = useState<Person[]>([])
    const [allPeople, setAllPeople] = useState<Person[]>([])
    const [sessionEmail, setSessionEmail] = useState(session.email)

    const params = useParams()
    const navigate = useNavigate()

    const activePage = params.pageNum ? parseInt(params.pageNum) : 1

    function setPage(activePage: number) {
        // Update the route to the new page number
        navigate(`/sessions/${session.id}/${activePage}`)
    }

    let companyInfo: JSX.Element
    if (company) {
        companyInfo = (
            <div>
                <h2>{company.company.name}</h2>
            </div>
        )
    } else {
        companyInfo = <div>Company not found</div>
    }

    function transformPeople(people: Person[]) {
        let peopleRecords: Person[]
        if (people) {
            peopleRecords = people.map((companyPerson) => {
                const data = companyPerson.person.data
                if (!data) {
                    throw new Error(
                        `Data for companyPerson not found ${companyPerson}`
                    )
                }

                return new Person(
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

    // When the people updates, update the selectedPeople
    // Note: This is a weird API for the DataTable imho, seems like the selected state should just be a prop
    useEffect(() => {
        const newAllPeople = transformPeople(people)
        setAllPeople(newAllPeople)

        const curSelectedPeople = newAllPeople.filter(
            (person) => person.selected
        )
        setSelectedPeople(curSelectedPeople)
    }, [people])

    const mainEmailRef = useRef<HTMLFormElement>(null)

    // Take the top email and sync it to all of the people
    function syncEmail() {
        console.log("syncing email")
        const newAllPeople = allPeople.map((person) => {
            if (mainEmailRef.current) {
                return {
                    ...person,
                    email: mainEmailRef.current.value,
                }
            } else {
                return person
            }
        })
        setAllPeople(newAllPeople)
    }

    // When the person changes the email message on an individual person
    function updateIndividualRecord(
        e: React.ChangeEvent<HTMLInputElement>,
        recordIndex: number,
        allPeople: Person[],
        setAllPeople: React.Dispatch<React.SetStateAction<Person[]>>
    ) {
        const updatedEmail = e.currentTarget.value

        setAllPeople((prevPeople) =>
            prevPeople.map((person, index) =>
                index === recordIndex
                    ? {
                          ...person,
                          email: updatedEmail,
                      }
                    : person
            )
        )
    }

    console.log("full re-render")

    return (
        <div>
            <form>
                {companyInfo}

                <Textarea
                    label="Email"
                    className="emailEditor"
                    minRows={8}
                    sx={{ height: "100%" }}
                    ref={mainEmailRef}
                    value={sessionEmail}
                    onChange={(e) => {
                        const newEmailText = e.currentTarget.value

                        // Save the email to the session
                        fetch(`/sessions/${session.id}`, {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify({
                                email: newEmailText,
                            }),
                        })

                        setSessionEmail(newEmailText)
                    }}
                />

                <Group position="right">
                    <Button onClick={(e) => syncEmail()} variant="light">
                        Copy to All
                    </Button>
                </Group>
                <Space h="lg" />
                <DataTable
                    withColumnBorders
                    striped
                    columns={[
                        { accessor: "name" },
                        { accessor: "current_title" },
                        { accessor: "normalized_title" },
                        {
                            accessor: "linkedin_url",
                            render: (url) => <a href={url}>LinkedIn</a>,
                        },
                    ]}
                    rowExpansion={{
                        content: ({ record, recordIndex }) => (
                            <Stack p="xs" spacing={10} h={250}>
                                <Textarea
                                    className="emailEditor"
                                    sx={{ height: "100%" }}
                                    onChange={(e) =>
                                        updateIndividualRecord(
                                            e,
                                            recordIndex,
                                            allPeople,
                                            setAllPeople
                                        )
                                    }
                                    value={record.email}
                                />
                            </Stack>
                        ),
                    }}
                    selectedRecords={selectedPeople}
                    onSelectedRecordsChange={setSelectedPeople}
                    records={allPeople}
                />
                <Button
                    onClick={(e) =>
                        savePeople(session, allPeople, selectedPeople)
                    }
                >
                    Save
                </Button>

                <Space h="lg" />
                <Pagination
                    value={activePage}
                    onChange={setPage}
                    total={totalPeople / perPage}
                />
            </form>
        </div>
    )
}
