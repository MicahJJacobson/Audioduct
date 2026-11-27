import subprocess
import asyncio
import pulsectl_asyncio
from pulsectl_asyncio import PulseAsync

# builder class for pulse instances
class PulseBuilder:

    _count: int = 0

    def __init__(self):
        raise RuntimeError("Call PulseBuilder.build() instead of the constructor")

    @classmethod
    async def build(cls):
        pulse = PulseAsync(f"pulse-{cls._count}")
        await pulse.connect()
        cls._count += 1
        return pulse

    @classmethod
    async def close(cls, pulseObject: PulseAsync):
        if isinstance(pulseObject, PulseAsync):
            pulseObject.close()
            pulseObject = None

    # The pulseaudio server keeps going down and I'm getting connection terminated even when I try to connect to the regular server on my computer. I need to have a way to restart it and refresh connection
    @classmethod
    async def reconnect(cls, pulseObject: PulseAsync):

        result = subprocess.run(
            ["pactl", "list", "sink-inputs"],
            capture_output=True,
            text=True,
        ) 

        if result.returncode != 0 or "Connection failure" in result:
            if "Connection terminated" in result.stderr:
                print("Got connection terminated error")
                print("Attempting to reconnect...")
                print("Resetting Audio Server")
                await cls.resetAudioServer()
                print("Audio server reset")
                #print("Closing old PulseAsync object...")
                #await cls.close(pulseObject)
                #print("Old PulseAsync object closed")
                #print("Building new PulseAsync object...")
                #pulseObject = await cls.build()
                #print("PulseAsync object built")
                print("Attempting to reconnect to the old PulseAsync object")
                await pulseObject.connect()
                print("Connected to old PulseAsync object")
                print("Returning PulseAsync object")
                return pulseObject
            else:
                print(f"pactl failed: {result.stderr.strip()}")
            return None
        return result.stdout

    @classmethod
    async def resetAudioServer(cls):
        subprocess.run(
            ["systemctl", "--user", "restart", "pipewire", "pipewire-pulse", "wireplumber"]
        )
