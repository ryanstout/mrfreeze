import type { LoaderArgs } from "@remix-run/node"
import { redirect } from "@remix-run/node"
import { z } from "zod"
import { zx } from "zodix"

// Redirect to the first company and person
export const loader = async ({ params }: LoaderArgs) => {
    let { sessionId } = zx.parseParams(params, { sessionId: z.string() })
    return redirect(`/sessions/${sessionId}/company/0/person/0`)
}
