from audioduct import Audioduct
import asyncio


class ApplicationGroupManager:

    def __init__(self):
        raise RuntimeError("ApplicationGroupManager is a static class. Call its methods using the class name")

    @classmethod
    async def listen_for_sink_inputs(self) -> void:
        pulse = await Audioduct.getInstance()
        async for event in pulse.subscribe_events("sink_input"):
            if event.t == "new":
                print("new stream, index ", event.index)
                #self.add_new_sink_input()

    # call pulsectl to find the sink_inputs that are currently running
    @classmethod
    async def find_client_sink_inputs(cls, client_index: int) -> list[PulseSinkInputInfo]:
        pulse = await Audioduct.getInstance()
        all_sink_inputs = await pulse.sink_input_list()
        sink_inputs = [sink_input for sink_input in all_sink_inputs if sink_input.client == client_index] # will loop through each sink_input and only add to the list the ones that match the client index that was input in the method
        return sink_inputs
        
    

asyncio.run(ApplicationGroupManager.find_client_sink_inputs(98))
