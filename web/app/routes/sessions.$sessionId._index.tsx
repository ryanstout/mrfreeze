import type { LoaderArgs } from "@remix-run/node"
import { redirect } from "@remix-run/node"
import { z } from "zod"
import { zx } from "zodix"
import { prisma } from "~/db.server"

// Redirect to the first company and person
export const loader = async ({ params }: LoaderArgs) => {
    let { sessionId } = zx.parseParams(params, { sessionId: z.string() })
    return redirect(`/sessions/${sessionId}/company/0/person/0`)
}

export async function action({ request, params }: LoaderArgs) {
    // const { sessionId } = zx.parseParams(params, { sessionId: z.string() })

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
