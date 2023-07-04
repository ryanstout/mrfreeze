import type { LoaderArgs } from "@remix-run/node"
import { useLoaderData } from "@remix-run/react"
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
            include: { people: { include: { person: true } } },
          },
        },
      },
    },
  })
}

export default function SessionIndex() {
  const session = useLoaderData<typeof loader>()
  if (!session) {
    return <div>Session not found</div>
  }

  return (
    <div>
      <h1>{session.name}</h1>

      {session.companies.length > 0 ? (
        <ul>
          {session.companies.map((session_company) => (
            <li key={session_company.id}>
              <h3>{session_company.company.name}</h3>

              {session_company.company.people.length > 0 ? (
                <ul>
                  {session_company.company.people.map((company_person) => (
                    <li key={company_person.id}>
                      {company_person.person.name}
                    </li>
                  ))}
                </ul>
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
