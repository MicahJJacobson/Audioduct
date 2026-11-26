from audioduct import Audioduct

class ApplicationGroups:

    _groups: dict[client_index: int, client: ApplicationGroup] = {}
    _owner_of: dict[int, int] = {} # This holds the sink index as the key and then the client index that owns it as a value

    def __init__(self):
        raise RuntimeError("Call ApplicationGroups.getInstance() instead of the ApplicationGroups constructor")

    # could not have add_sink_input in this file to prevent circular import. Had to use this to give ApplicationGroupManager access to the groups
    @classmethod
    def get_application_group_from_client_index(cls, client_index: int) -> ApplicationGroup | None:
        return cls._groups.get(client_index)

    @classmethod 
    def get_client_index_from_sink_input_index(cls, sink_index: int) -> int | None:
        return cls._owner_of.get(sink_index)

    @classmethod 
    def get_application_group_from_sink_input_index(cls, sink_index: int) -> ApplicationGroup | None:
        client_index = cls.get_client_index_from_sink_input_index(sink_index)
        application_group = cls.get_application_group_from_client_index(client_index)
        return application_group

    @classmethod
    def get_sink_input_from_sink_input_index(cls, sink_index: int) -> PulseSinkInputInfo:
        application_group = cls.get_application_group_from_sink_input_index(sink_index)
        if application_group is None:
            return None
        for sink_input in application_group.sink_inputs:
            if sink_input.index == sink_index:
                return sink_input
        return None

    @classmethod
    def add_application_group(cls, group: ApplicationGroup):
        client = group.client
        sink_inputs = group.sink_inputs
        cls._groups[client.index] = group
        for sink_input in sink_inputs: # populates the _owner_of dictionary so that we have the corresponding client index for every sink_input index
            cls.record_sink_input_owner(sink_input)

    # record the client that owns this sink in the _owner_of dictionary
    @classmethod
    def record_sink_input_owner(cls, sink_input: PulseSinkInputInfo) -> void:
        cls._owner_of[sink_input.index] = sink_input.client

    # forget the record of the client that owns this sink in the _owner_of dictionary
    @classmethod
    def forget_sink_input_owner(cls, sink_input: PulseSinkInputInfo) -> void:
        cls._owner_of.pop(sink_input.index)

    @classmethod
    def print_client_short(cls, client_index: int):
        print(f"Client: {cls._groups.get(client_index).client.name} {client_index}", end="")
        for i in range(5):
            print(" ", end="")
        print("sink_inputs: ", end="")
        application_group = ApplicationGroups.get_application_group_from_client_index(client_index)
        sink_inputs = application_group.sink_inputs
        for sink_input in sink_inputs:
            print(f"{{Name: {sink_input.name}, Index: {sink_input.index}}}, ", end="")
        print("")
