import { exec as execCb } from "child_process"
import { promisify } from "util"

const exec = promisify(execCb)

interface ExecOptions {
    cwd?: string
}

export async function runCommand(
    command: string,
    workingDir: string = "."
): Promise<string> {
    try {
        const options: ExecOptions = { cwd: workingDir }
        const { stdout, stderr } = await exec(command, options)

        if (stderr) {
            throw new Error(`Error: ${stderr}`)
        }

        return stdout
    } catch (error) {
        throw error
    }
}
