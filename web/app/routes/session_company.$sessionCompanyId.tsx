import { redirect, type LoaderArgs } from "@remix-run/node"
import qs from "qs"
import { z } from "zod"
import { zx } from "zodix"
import { prisma } from "~/db.server"

type ParserFunction = (
    params: URLSearchParams
) => Record<string, string | string[]>
const customParser: ParserFunction = async () => {
    qs.parse(await request.text())
}

export async function action({ request, params }: LoaderArgs) {
    // const body = await request.formData()
    // console.log("form: ", JSON.stringify(body.entries()))

    // const res = qs.parse(await request.text())
    // console.log(res)

    const { sessionCompanyId } = await zx.parseParams(params, {
        sessionCompanyId: z.string(),
    })

    // get the company session
    const sessionCompany = await prisma.sessionCompany.findFirst({
        where: { id: sessionCompanyId },
    })

    if (!sessionCompany) {
        throw new Error("Session Company not found")
    }
    // Zodix has issues parsing nested form stuff, so use qs to parse the form data and zod for objects
    const formParams = qs.parse(await request.text())

    const formCompanyPersonObject = z.object({
        id: z.string(),
        selected: z.string().optional(),
    })

    const formCompanyPeople = z
        .array(formCompanyPersonObject)
        .parse(formParams.people)

    const companyPersons = await prisma.companyPerson.findMany({
        where: {
            sessionId: sessionCompany.sessionId,
            companyId: sessionCompany.companyId,
        },
        include: { person: true },
    })

    for await (const companyPerson of companyPersons) {
        // Match to form data
        const formCompanyPerson = formCompanyPeople.find(
            (p) => p.id === companyPerson.id
        )
        if (formCompanyPerson) {
            await prisma.companyPerson.update({
                where: { id: companyPerson.id },
                data: {
                    selected: !!formCompanyPerson.selected,
                },
            })
        }
    }

    return redirect(`/sessions/${sessionCompany?.sessionId}`)
}

export default function CompanyPerson() {
    return <h1>Company Person</h1>
}
