from audioduct import Audioduct
import asyncio


class ApplicationGroupManager:

    def __init__(self):
        print("initializing ApplicationGroupManager")

    async def listen_for_sink_inputs(self):
        pulse = await Audioduct.getInstance()
        async for event in pulse.subscribe_events("sink_input"):
            if event.t == "new":
                print("new stream, index ", event.index)
                #self.add_new_sink_input()

    

asyncio.run(listen_for_sink_inputs())
