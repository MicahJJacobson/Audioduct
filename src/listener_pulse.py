import subprocess
import asyncio
import pulsectl_asyncio
from pulsectl_asyncio import PulseAsync

# builder class for pulse instances
class ListenerPulse:

    _count: int = 0

    def __init__(self):
        raise RuntimeError("Call ListenerPulse.build() instead of the constructor")

    @classmethod
    async def build(cls):
        pulse = PulseAsync(f"listener-{cls._count}")
        await pulse.connect()
        cls._count += 1
        return pulse

