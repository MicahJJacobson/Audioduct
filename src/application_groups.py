from audioduct import Audioduct

class ApplicationGroups:

    _groups: dict[client_index: int, client: ApplicationGroup] = {}

    def __init__(self):
        raise RuntimeError("Call ApplicationGroups.getInstance() instead of the ApplicationGroups constructor")

    #@classmethod
    #def getInstance(cls):
    #    if not cls._groups:
    #        cls._groups = {}
    #        return cls._groups
    #    else:
    #        return cls._groups

    # could not have add_sink_input in this file to prevent circular import. Had to use this to give ApplicationGroupManager access to the groups
    @classmethod
    def get_application_group(cls, client_index: int) -> ApplicationGroup | None:
        return cls._groups.get(client_index)

    @classmethod
    def add_application_group(cls, group: ApplicationGroup):
        client = group.client
        sink_inputs = group.sink_inputs
        cls._groups[client.index] = group

    #@classmethod
    #async def add_sink_input(cls, sink_input: PulseSinkInputInfo):
    #    pulse = await Audioduct.getInstance()
    #    if sink_input.client in cls._groups:  # if the client for this sink_input is already in _groups, add this to the sink_input list of that client. Otherwise, make a new ApplicationGroup with this client
    #        application_group = cls._groups[sink_input.client]
    #        application_group.add_sink_input(sink_input)
    #    else:
    #        client = await pulse.client_info(sink_input.client)
    #        if not client: # If the client doesn't exist
    #            raise RuntimeError(f"Client {sink_input.client} does not exist")
    #        else:
    #            ApplicationGroupManager.build_application_group(sink_input.client)


