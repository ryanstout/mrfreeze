import { redirect, type LoaderArgs } from "@remix-run/node"
import path from "path"
import qs from "qs"
import { z } from "zod"
import { zx } from "zodix"
import { prisma } from "~/db.server"
import { runCommand } from "~/utils.server"

type ParserFunction = (
    params: URLSearchParams
) => Record<string, string | string[]>
const customParser: ParserFunction = async () => {
    qs.parse(await request.text())
}

export async function action({ request, params }: LoaderArgs) {
    const { sessionId } = await zx.parseParams(params, {
        sessionId: z.string(),
    })

    const session = await prisma.session.findFirst({
        where: { id: sessionId },
    })

    if (!session) {
        throw new Error("Session not found")
    }

    // Update all CompanyPerson's in the session as ready to send if selected
    await prisma.companyPerson.updateMany({
        where: {
            sessionId: session.id,
            selected: true,
        },
        data: {
            readyToSend: true,
        },
    })

    const parentDir = path.resolve(process.cwd(), "..")

    // shell out to python to create the drafts
    const command = `PRISMA_PY_DEBUG_GENERATOR=1 python -m src.send_emails ${JSON.stringify(
        session.id
    )}`

    const stdout = await runCommand(command, parentDir)
    console.log("stdout: ", stdout)

    return redirect(`/`)
}

export default function CompanyPerson() {
    return <h1>Company Person</h1>
}
