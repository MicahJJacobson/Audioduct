import asyncio

async def async_function():
    #command = ["systemctl", "--user", "restart", "pipewire", "pipewire-pulse", "wireplumber"]
    command = ["echo", "hello", "world"]

    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    out, err = await process.communicate()

    print(f"returncode={process.returncode} stdout={out.decode()!r} stderr={err.decode()!r}")

    #if process.returncode != 0:
    #    raise RuntimeError(f"Failed to restart audio server: {stderr.decode().strip()}")

asyncio.run(async_function())
