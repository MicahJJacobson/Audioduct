import subprocess
import asyncio
import pulsectl_asyncio
from pulsectl_asyncio import PulseAsync
from pulse_builder import PulseBuilder

# Singleton class for the PulseAsync object
class Audioduct:

    _pulse: PulseAsync | None = None

    def __init__(self):
        raise RuntimeError("Call Audioduct.getInstance() instead of calling the Audioduct constructor")

    @classmethod
    async def getInstance(cls):
        if not cls._pulse:
            cls._pulse = await PulseBuilder.build()
            return cls._pulse
        else:
            return cls._pulse

    @classmethod
    async def close(cls):
        if cls._pulse is not None:
            await PulseBuilder.close(cls._pulse)
            cls._pulse = None

    @classmethod
    async def reconnect(cls):
        try:
            cls._pulse = await cls.getInstance()
            clients = await cls._pulse.client_list()
            return cls._pulse
        except PulseError as e:
            print(e)
            cls._pulse = await PulseBuilder.reconnect(cls._pulse)
            return cls._pulse

