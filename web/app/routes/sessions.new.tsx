import { Button, Space, TextInput } from "@mantine/core"
import { redirect, type ActionArgs } from "@remix-run/node"
import { Form } from "@remix-run/react"
import path from "path"
import { z } from "zod"
import { zx } from "zodix"
import { prisma } from "~/db.server"
import { runCommand } from "~/utils.server"

// Create a new session, use python to search for companies
export async function action({ request }: ActionArgs) {
    const { name, company_search_keyword, person_search_keyword } =
        await zx.parseForm(request, {
            name: z.string(),
            company_search_keyword: z.string(),
            person_search_keyword: z.string(),
        })

    const newSession = await prisma.session.create({
        data: {
            name: name,
            company_search_keyword: company_search_keyword,
            person_search_keyword: person_search_keyword,
        },
    })

    // Get the parent directory
    const parentDir = path.resolve(process.cwd(), "..")

    // use JSON.stringify to escape strings
    const command = `PRISMA_PY_DEBUG_GENERATOR=1 python -m bin.fetch_companies_and_people ${JSON.stringify(
        newSession.id
    )} ${JSON.stringify(company_search_keyword)} ${JSON.stringify(
        person_search_keyword
    )}`

    console.log("run command: ", command)
    await runCommand(command, parentDir)

    // redirect to /sessions/{name}
    return redirect(`/sessions/${newSession.id}`)
}

export default function New() {
    return (
        <div>
            <h1>New Session</h1>

            <Form method="post">
                <TextInput label="Name" name="name" required />
                <TextInput
                    label="Company Search Keyword"
                    name="company_search_keyword"
                    required
                />
                <TextInput
                    label="Person Search Keywords"
                    name="person_search_keyword"
                    description="I'm looking for people in charge of [keywords]"
                    required
                />
                <Space h="lg" />
                <Button type="submit">Create</Button>
            </Form>
        </div>
    )
}
