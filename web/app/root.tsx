import { Container, MantineProvider, createEmotionCache } from "@mantine/core"
import { StylesPlaceholder } from "@mantine/remix"
import { cssBundleHref } from "@remix-run/css-bundle"
import type { LinksFunction, LoaderArgs } from "@remix-run/node"
import { json } from "@remix-run/node"
import {
    Links,
    LiveReload,
    Meta,
    Outlet,
    Scripts,
    ScrollRestoration,
} from "@remix-run/react"

import { getUser } from "~/session.server"
import stylesheet from "~/stylesheet.css"
import { HeaderSimple } from "./routes/header_simple"

createEmotionCache({ key: "mantine" })

export const links: LinksFunction = () => [
    { rel: "stylesheet", href: stylesheet },
    ...(cssBundleHref ? [{ rel: "stylesheet", href: cssBundleHref }] : []),
]

export const loader = async ({ request }: LoaderArgs) => {
    return json({ user: await getUser(request) })
}

export default function App() {
    return (
        <MantineProvider withGlobalStyles withNormalizeCSS>
            <html lang="en">
                <head>
                    <meta charSet="utf-8" />
                    <meta
                        name="viewport"
                        content="width=device-width,initial-scale=1"
                    />
                    <StylesPlaceholder />
                    <Meta />
                    <Links />
                </head>
                <body>
                    <Container>
                        <HeaderSimple
                            links={[
                                { link: "/", label: "Sessions" },
                                { link: "/sessions/new", label: "New Session" },
                            ]}
                        />
                        <Outlet />
                    </Container>
                    <ScrollRestoration />
                    <Scripts />
                    <LiveReload />
                </body>
            </html>
        </MantineProvider>
    )
}
