import subprocess
import asyncio
import pulsectl_asyncio
from pulsectl_asyncio import PulseAsync

# Singleton class for the PulseAsync object
class Audioduct:

    _pulse: PulseAsync | None = None

    def __init__(self):
        raise RuntimeError("Call Audioduct.getInstance() instead of calling the Audioduct constructor")

    @classmethod
    async def getInstance(cls):
        if not cls._pulse:
            cls._pulse = PulseAsync("Audioduct-client")
            await cls._pulse.connect()
            return cls._pulse
        else:
            return cls._pulse

    @classmethod
    def close(cls):
        if cls._pulse is not None:
            cls._pulse.close()
            cls._pulse = None

    @classmethod
    async def reconnect(cls):
        try:
            cls._pulse = cls.getInstance()
            clients = pulse.client_list()
        except:
            cls.close()
            cls._pulse = PulseAsync("Audioduct-client")
            await cls._pulse.connect()
            return cls._pulse

