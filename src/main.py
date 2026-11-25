from audioduct import Audioduct
import asyncio
import typer
#def make_channel(name: str, real_sink: str):
#    subprocess.run("pactl", "load-module", "module-null-sink", f"sink-name={name}", f"sink-properties=device.description={name}")

async def main():
    await list_sinks()

async def list_sinks():
    pulse = await Audioduct.getInstance();
    streams = await pulse.sink_input_list()

if __name__ == "__main__":
    asyncio.run(main())
