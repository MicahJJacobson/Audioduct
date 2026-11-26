from audioduct import Audioduct
import asyncio

class ApplicationGroup:

    _client: PulseClientInfo
    _sink_inputs: list[PulseSinkInputInfo]

    def __init__(self, client: PulseClientInfo, sink_inputs: list[PulseSinkInputInfo]):
        self._client = client
        self._sink_inputs = sink_inputs

    @property
    def client(self):
        return self._client
    
    @property
    def sink_inputs(self):
        return self._sink_inputs

    def add_sink_input(self, sink_input: PulseSinkInputInfo) -> void:
        self._sink_inputs.append(sink_input)

    def remove_sink_input(self, sink_input: PulseSinkInputInfo) -> void:
        self._sink_inputs.remove(sink_input)

    # this will entirely replace a sink with a new one that has a matching index
    def update_sink_input(self, sink_input: PulseSinkInputInfo) -> void:
        for i, existing in enumerate(self._sink_inputs):
            if existing.index == sink_input.index:
                self._sink_inputs[i] = sink_input
                return True
        return False

#async def testThatClientAndStreamsPrint():
#    pulse = await Audioduct.getInstance()
#    clients = await pulse.client_list()
#    print(clients)
#    streams = await pulse.sink_input_list()
#    group = ApplicationGroup(clients[0], streams)

#asyncio.run(testThatClientAndStreamsPrint())
