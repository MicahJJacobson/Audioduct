from audioduct import Audioduct

class ApplicationGroups:

    _groups: dict[client_index: int, client: ApplicationGroup] = {}

    def __init__(self):
        rasie RuntimeError("Call ApplicationGroups.getInstance() instead of the ApplicationGroups constructor")

    @classmethod
    def getInstance(cls):
        if not cls._groups:
            cls._groups = {}
            return cls._groups
        else:
            return cls._groups

    @classmethod
    def add_application_group(self, group: ApplicationGroup):
        client = group.client
        streams = group.streams
        _groups[client.index] = group
