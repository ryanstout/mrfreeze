import { Box, Button, Checkbox, Group, Table } from "@mantine/core"
import type { CompanyPerson } from "@prisma/client"
import type { LoaderArgs } from "@remix-run/node"
import { Form, useLoaderData, useSubmit } from "@remix-run/react"
import { z } from "zod"
import { zx } from "zodix"
import { prisma } from "~/db.server"

export async function loader({ params }: LoaderArgs) {
    const { id } = zx.parseParams(params, { id: z.string() })

    return await prisma.session.findFirst({
        where: { id: id },
        include: {
            companies: {
                include: {
                    company: {
                        include: {
                            people: {
                                include: {
                                    person: {
                                        select: {
                                            id: true,
                                            name: true,
                                            data: true,
                                        },
                                    },
                                },
                                orderBy: { createdAt: "asc" },
                            },
                        },
                    },
                },
            },
        },
    })
}

function CompanyPersonRow({
    companyPerson,
    index,
}: {
    companyPerson: CompanyPerson
    index: number
}) {
    return (
        <tr key={companyPerson.id}>
            <td>
                <input
                    type="hidden"
                    name={`people[${index}][id]`}
                    value={companyPerson.id}
                />
                <Checkbox
                    name={`people[${index}][selected]`}
                    value={companyPerson.id}
                    defaultChecked={companyPerson.selected}
                />
            </td>
            <td>{companyPerson.person.name}</td>
            <td>{companyPerson.person.data.current_title}</td>
            <td>{companyPerson.person.data.normalized_title}</td>
            <td>
                <a href={companyPerson.person.data.linkedin_url}>LinkedIn</a>
            </td>
        </tr>
    )
}

export default function SessionIndex() {
    const session = useLoaderData<typeof loader>()
    if (!session) {
        return <div>Session not found</div>
    }

    const submit = useSubmit()

    return (
        <div>
            <h1>{session.name}</h1>

            {session.companies.length > 0 ? (
                <ul>
                    {session.companies.map((session_company) => (
                        <li key={session_company.id}>
                            <Group grow>
                                <h3>{session_company.company.name}</h3>
                                <Box sx={{ textAlign: "right" }}>
                                    {session_company.company.data.industry_str}
                                </Box>
                            </Group>

                            {session_company.company.people.length > 0 ? (
                                <Form
                                    method="post"
                                    action={`/session_company/${session_company.id}`}
                                >
                                    <Table verticalSpacing="xs">
                                        <thead>
                                            <tr>
                                                <th></th>
                                                <th>Name</th>
                                                <th>Current Title</th>
                                                <th>Normalized Title</th>
                                                <th></th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {session_company.company.people.map(
                                                (company_person, index) => (
                                                    <CompanyPersonRow
                                                        key={company_person.id}
                                                        companyPerson={
                                                            company_person
                                                        }
                                                        index={index}
                                                    />
                                                )
                                            )}
                                        </tbody>
                                    </Table>

                                    <Button type="submit">Save</Button>
                                </Form>
                            ) : (
                                <div>No people found</div>
                            )}
                        </li>
                    ))}
                </ul>
            ) : (
                <div>No companies found</div>
            )}
        </div>
    )
}
