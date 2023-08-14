import type { ChildProcessWithoutNullStreams } from "child_process"
import { spawn } from "child_process"
import { parse } from "shell-quote"

export function runCommand(commandStr: string, cwd?: string): Promise<boolean> {
    return new Promise((resolve, reject) => {
        let env: NodeJS.ProcessEnv = { ...process.env }

        // Extract environment variables from the command string.
        const envPattern: RegExp = /^([A-Z_]+[A-Z0-9_]*)=(\S+)\s/i
        let match: RegExpExecArray | null
        while ((match = envPattern.exec(commandStr))) {
            env[match[1]] = match[2]
            commandStr = commandStr.replace(match[0], "") // remove the env var from the command
        }

        // Parse the command string into command and arguments.
        const parts: string[] = parse(commandStr)
        if (parts.length === 0) {
            reject(new Error("No command provided."))
            return
        }

        const cmd: string = parts[0]
        const args: string[] = parts.slice(1)

        const child: ChildProcessWithoutNullStreams = spawn(cmd, args, {
            env: env, // set the environment variables
            cwd: cwd, // set the current working directory
        })

        // Print stdout as lines come in
        child.stdout.on("data", (data: Buffer) => {
            process.stdout.write(data)
        })

        // Print stderr as lines come in
        child.stderr.on("data", (data: Buffer) => {
            process.stderr.write(data)
        })

        child.on("exit", (code: number | null) => {
            resolve(code === 0)
        })

        child.on("error", (err: Error) => {
            reject(err)
        })
    })
}
