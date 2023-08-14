import {
    Button,
    Grid,
    Group,
    Pagination,
    Space,
    Stack,
    Textarea,
} from "@mantine/core"
import type { Session } from "@prisma/client"
import type { LoaderArgs } from "@remix-run/node"
import { useLoaderData, useNavigate, useParams } from "@remix-run/react"
import { DataTable } from "mantine-datatable"
import { useEffect, useRef, useState } from "react"
import { z } from "zod"
import { zx } from "zodix"
import { prisma } from "~/db.server"
import type { FullPerson } from "../utils/people_utils"
import { savePeople, transformPeople } from "../utils/people_utils"

const peoplePerPage = 20
const companiesPerPage = 1

export async function loader({ params }: LoaderArgs) {
    const { sessionId, companyPageNum, personPageNum } = zx.parseParams(
        params,
        {
            sessionId: z.string(),
            companyPageNum: zx.NumAsString.optional(),
            personPageNum: zx.NumAsString.optional(),
        }
    )

    const session = await prisma.session.findFirst({
        where: { id: sessionId },
    })

    if (!session) {
        throw new Error("Session not found")
    }

    console.log("session: ", session, " find: ", session.id)

    // Fetch the first company
    const companies = await prisma.sessionCompany.findMany({
        where: { sessionId: session.id },
        include: {
            company: true,
        },
        skip: companyPageNum ? companyPageNum : 0,
    })

    if (!companies || companies.length === 0) {
        throw new Error("Company not found")
    }

    const totalCompanies = await prisma.sessionCompany.count({
        where: { sessionId: session.id },
    })

    const company = companies[0]

    // Get the CompanyPerson for the company that match this session
    const people = await prisma.companyPerson.findMany({
        where: {
            sessionId: session.id,
            companyId: company.companyId,
        },
        include: { person: true },
        // limit/offset by pageNum and perPage
        take: peoplePerPage,
        skip: personPageNum ? personPageNum * peoplePerPage : 0,
        orderBy: { createdAt: "asc" },
    })

    const totalPeople = await prisma.companyPerson.count({
        where: {
            sessionId: session.id,
            companyId: company.companyId,
        },
    })

    return { session, company, totalCompanies, people, totalPeople }
}

export default function SessionIndex() {
    const { session, company, totalCompanies, people, totalPeople } =
        useLoaderData<typeof loader>()

    const [selectedPeople, setSelectedPeople] = useState<FullPerson[]>([])
    const [allPeople, setAllPeople] = useState<FullPerson[]>([])
    const [sessionEmail, setSessionEmail] = useState(session.email)

    const params = useParams()
    const navigate = useNavigate()

    const activePersonPage = params.personPageNum
        ? parseInt(params.personPageNum)
        : 0
    const activeCompanyPage = params.companyPageNum
        ? parseInt(params.companyPageNum)
        : 0

    function setPage({
        newPersonPageNum = activePersonPage,
        newCompanyPageNum = activeCompanyPage,
    }: {
        newPersonPageNum?: number
        newCompanyPageNum?: number
    }) {
        if (newCompanyPageNum !== activeCompanyPage) {
            // When changing companies, set the person page to 0
            newPersonPageNum = 0
        }

        navigate(
            `/sessions/${session.id}/company/${newCompanyPageNum}/person/${newPersonPageNum}`
        )
    }

    function nextPage() {
        if (activePersonPage < totalPeople / peoplePerPage - 1) {
            setPage({ newPersonPageNum: activePersonPage + 1 })
        } else if (activeCompanyPage < totalCompanies / companiesPerPage - 1) {
            setPage({
                newCompanyPageNum: activeCompanyPage + 1,
                newPersonPageNum: 0,
            })
        }
    }

    function previousPage() {
        if (activePersonPage > 0) {
            setPage({ newPersonPageNum: activePersonPage - 1 })
        } else if (activeCompanyPage > 0) {
            setPage({
                newCompanyPageNum: activeCompanyPage - 1,
                newPersonPageNum: 0,
            })
        }
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

    // Hotkey listener for CMD + ENTER
    useEffect(() => {
        const handleKeyDown = (e) => {
            // Check for CMD (or CTRL) + ENTER key press
            if ((e.metaKey || e.ctrlKey) && e.keyCode === 13) {
                if (e.shiftKey) {
                    savePeople(session, allPeople, selectedPeople, previousPage)
                } else {
                    savePeople(session, allPeople, selectedPeople, nextPage)
                }
            }
        }

        // Add the event listener to the `document`
        document.addEventListener("keydown", handleKeyDown)

        // Cleanup the event listener on component unmount
        return () => {
            document.removeEventListener("keydown", handleKeyDown)
        }
    }, [allPeople, selectedPeople]) // Empty dependency array ensures the effect runs once after the component mounts

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
        allPeople: FullPerson[],
        setAllPeople: React.Dispatch<React.SetStateAction<FullPerson[]>>
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

    async function createDrafts(session: Session) {
        await fetch(`/send_email/${session.id}`, {
            method: "POST",
        })
    }

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
                <Group sx={{ padding: 10 }}>
                    <Button
                        onClick={(e) =>
                            savePeople(
                                session,
                                allPeople,
                                selectedPeople,
                                previousPage
                            )
                        }
                    >
                        Previous (CMD + SHIFT + ENTER)
                    </Button>
                    <Button
                        onClick={(e) =>
                            savePeople(
                                session,
                                allPeople,
                                selectedPeople,
                                nextPage
                            )
                        }
                    >
                        Next (CMD + ENTER)
                    </Button>
                </Group>

                <Space h="lg" />
                <Grid justify="space-between">
                    <Grid justify="center">
                        <p>People: &nbsp;</p>
                        <Pagination
                            position="center"
                            value={activePersonPage + 1}
                            onChange={(pageNum) =>
                                setPage({ newPersonPageNum: pageNum - 1 })
                            }
                            total={Math.ceil(totalPeople / peoplePerPage)}
                        />
                    </Grid>

                    <Grid justify="center">
                        <p>Companies: &nbsp;</p>
                        <Pagination
                            value={activeCompanyPage + 1}
                            onChange={(pageNum) => {
                                setPage({ newCompanyPageNum: pageNum - 1 })
                            }}
                            total={Math.ceil(totalCompanies / companiesPerPage)}
                        />
                    </Grid>

                    <Button
                        onClick={() => {
                            createDrafts(session)
                        }}
                    >
                        Finished, Create Drafts
                    </Button>
                </Grid>
            </form>
        </div>
    )
}
