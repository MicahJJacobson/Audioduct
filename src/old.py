from audioduct import Audioduct
import asyncio
import typer
#def make_channel(name: str, real_sink: str):
#    subprocess.run("pactl", "load-module", "module-null-sink", f"sink-name={name}", f"sink-properties=device.description={name}")

typerApp = typer.Typer()

async def main():
    await list_sinks()

async def list_sinks():
    pulse = await Audioduct.getInstance();
    streams = await pulse.sink_input_list()

@typerApp.command()
def hello(name: str, iq: int, display_iq: bool = True):
    print(f"Hello {name}")
    if display_iq:
        print(f"You have an IQ of {iq}")
    asyncio.run(main())

@typerApp.command()
def goodbye():
    print("goodbye")

if __name__ == "__main__":
    typerApp()
