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

#async def testThatClientAndStreamsPrint():
#    pulse = await Audioduct.getInstance()
#    clients = await pulse.client_list()
#    print(clients)
#    streams = await pulse.sink_input_list()
#    group = ApplicationGroup(clients[0], streams)

#asyncio.run(testThatClientAndStreamsPrint())
