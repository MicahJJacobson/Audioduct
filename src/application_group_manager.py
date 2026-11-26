from audioduct import Audioduct
import asyncio
from application_groups import ApplicationGroups
from application_group import ApplicationGroup


class ApplicationGroupManager:

    def __init__(self):
        raise RuntimeError("ApplicationGroupManager is a static class. Call its methods using the class name")

    @classmethod
    async def listen_for_sink_inputs(cls) -> void:
        pulse = await Audioduct.getInstance()
        #groups = await ApplicationGroups.getInstance() 
        async for event in pulse.subscribe_events("sink_input"):
            if event.t == "new":
                print(f"new stream, index {event.index}")
                sink_input = await pulse.sink_input_info(event.index)
                await cls.add_sink_input(sink_input)
            elif event.t == "remove":
                print(f"remove stream, index {event.index}")
                sink_input = ApplicationGroups.get_sink_input_from_sink_input_index(event.index) 
                await cls.remove_sink_input(sink_input)

    @classmethod
    async def initialize(cls):
        pulse = await Audioduct.getInstance()
        all_sink_inputs: list[PulseSinkInputInfo] = await pulse.sink_input_list()
        for sink_input in all_sink_inputs:
            await cls.add_sink_input(sink_input)

    # call pulsectl to find the sink_inputs that are currently running
    @classmethod
    async def find_client_sink_inputs(cls, client_index: int) -> list[PulseSinkInputInfo]:
        pulse = await Audioduct.getInstance()
        all_sink_inputs = await pulse.sink_input_list()
        sink_inputs = [sink_input for sink_input in all_sink_inputs if sink_input.client == client_index] # will loop through each sink_input and only add to the list the ones that match the client index that was input in the method
        return sink_inputs

    # this will build a new ApplicationGroup based on the client_index given
    @classmethod
    async def build_application_group(cls, client_index: int) -> ApplicationGroup:
        pulse = await Audioduct.getInstance()
        #groups = await ApplicationGroups.getInstance()
        all_clients = await pulse.client_list()
        client = await pulse.client_info(client_index)
        sink_inputs = await cls.find_client_sink_inputs(client_index)
        new_application_group = ApplicationGroup(client, sink_inputs)
        ApplicationGroups.add_application_group(new_application_group)
        return new_application_group
      
    # had to put add_sink_input in ApplicationGroupManager to prevent circular import
    @classmethod
    async def add_sink_input(cls, sink_input: PulseSinkInputInfo) -> void:
        pulse = await Audioduct.getInstance()
        application_group = ApplicationGroups.get_application_group_from_client_index(sink_input.client) # get the group that corresponds to this client index
        if application_group:  # if the client for this sink_input is already in _groups, add this to the sink_input list of that client. Otherwise, make a new ApplicationGroup with this client
            if ApplicationGroups.get_sink_input_from_sink_input_index(sink_input.index) is not None: # already exists in the dictionary
               return 
            else:
                application_group.add_sink_input(sink_input)
                ApplicationGroups.record_sink_input_owner(sink_input)
        else:
            client = await pulse.client_info(sink_input.client)
            if not client: # If the client doesn't exist
                raise RuntimeError(f"Client {sink_input.client} does not exist")
                return
            else: # if the client exists but isn't in ApplicationGroups, build the ApplicationGroup and add it
                application_group = await cls.build_application_group(sink_input.client)
         
        client_index = ApplicationGroups.get_client_index_from_sink_input_index(sink_input.index)
        ApplicationGroups.print_client_short(client_index)
        #print(application_group.client)
        #print(application_group.sink_inputs)

    @classmethod
    async def remove_sink_input(cls, sink_input: PulseSinkInputInfo) -> void:
        pulse = await Audioduct.getInstance()
        application_group = ApplicationGroups.get_application_group_from_client_index(sink_input.client)
        if application_group:
            application_group.remove_sink_input(sink_input)
            ApplicationGroups.forget_sink_input_owner(sink_input)
        else:
            raise RuntimeError(f"Application group for sink {sink_input} not found")
        client_index = application_group.client.index 
        ApplicationGroups.print_client_short(client_index)


#asyncio.run(ApplicationGroupManager.listen_for_sink_inputs())
