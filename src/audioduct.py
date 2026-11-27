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
            _pulse = PulseAsync("Audioduct-client")
            await _pulse.connect()
            return _pulse
        else:
            return _pulse

    @classmethod
    def close(cls):
        if cls._pulse is not None:
            _pulse.close()
            _pulse = None

    @classmethod
    async def reconnect(cls):
        try:
            pulse = cls.getInstance()
            clients = pulse.client_list()
        except:
            _pulse = PulseAsync("Audioduct-client")
            await _pulse.connect()
            return _pulse

