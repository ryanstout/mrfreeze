import type { V2_MetaFunction } from "@remix-run/node"
import { prisma } from "~/db.server"

import { Link, useLoaderData } from "@remix-run/react"

export const meta: V2_MetaFunction = () => [{ title: "MrFreeze Cold Emailer" }]

export const loader = async () => {
  return await prisma.session.findMany({})
}

export default function Index() {
  const sessions = useLoaderData<typeof loader>()

  return (
    <main>
      <div>
        <h1>Index</h1>

        {sessions.map((session) => (
          <div key={session.id}>
            <Link to={`/sessions/${session.id}`}>{session.name}</Link>
          </div>
        ))}
      </div>
    </main>
  )
}