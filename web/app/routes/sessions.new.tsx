import { Button, TextInput } from "@mantine/core"
import { redirect, type ActionArgs } from "@remix-run/node"
import { Form } from "@remix-run/react"
import { z } from "zod"
import { zx } from "zodix"
import { prisma } from "~/db.server"

export async function action({ request }: ActionArgs) {
  const { name, company_search_keyword } = await zx.parseForm(request, {
    name: z.string(),
    company_search_keyword: z.string(),
  })

  const newSession = await prisma.session.create({
    data: {
      name: name,
      company_search_keyword: company_search_keyword,
    },
  })

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
        <Button type="submit">Create</Button>
      </Form>
    </div>
  )
}
