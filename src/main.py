from audioduct import Audioduct
import asyncio
import typer
from application_group_manager import ApplicationGroupManager
#def make_channel(name: str, real_sink: str):
#    subprocess.run("pactl", "load-module", "module-null-sink", f"sink-name={name}", f"sink-properties=device.description={name}")

async def main():
    await ApplicationGroupManager.initialize()
    await ApplicationGroupManager.listen_for_sink_inputs()

async def list_sinks():
    pulse = await Audioduct.getInstance();

if __name__ == "__main__":
    asyncio.run(main())
