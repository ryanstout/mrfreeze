import { Outlet } from "@remix-run/react"
import { z } from "zod"
import { zx } from "zodix"
import { prisma } from "~/db.server"

export async function action({ request, params }: LoaderArgs) {
    const { id } = zx.parseParams(params, { id: z.string() })

    const data = JSON.parse(await request.text())

    // update the sessoion email in the database
    await prisma.session.update({
        where: { id: id },
        data: {
            email: data.email,
        },
    })

    return null
}

export default function SessionIndex() {
    return <Outlet />
}
