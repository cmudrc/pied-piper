from piperabm.object import PureObject
from piperabm.matter_new import Matter
from piperabm.time import DeltaTime


class Market(PureObject):

    section = "infrastructure"
    category = "node"
    type = "market"

    def __init__(
        self,
        pos: list = None,
        name: str = "",
        degradation: float = 0,
        resources = Matter({'food': 0, 'water': 0, 'energy': 0}),
        resources_influx =  Matter({'food': 0, 'water': 0, 'energy': 0}),
    ):
        super().__init__()
        
        self.infrastructure = None  # to access model

        self.pos = pos
        self.name = name
        self.degradation = degradation
        if isinstance(resources, dict):
            matter = Matter(resources)
            resources = matter
        if isinstance(resources, Matter):
            self.resources = resources
        else:
            raise ValueError
        if isinstance(resources_influx, dict):
            matter = Matter(resources_influx)
            resources_influx = matter
        if isinstance(resources_influx, Matter):
            self.resources_influx = resources_influx
        else:
            raise ValueError
        
    def update(self, duration):
        if isinstance(duration, DeltaTime):
            delta = duration.total_seconds()
        elif isinstance(duration, (int, float)):
            delta = duration
        delta_resources = self.resources_influx * delta
        self.resources + delta_resources

    def serialize(self) -> dict:
        dictionary = {}
        dictionary["pos"] = self.pos
        dictionary["name"] = self.name
        dictionary["degradation"] = self.degradation
        dictionary["resources"] = self.resources.serialize()
        dictionary["resources_influx"] = self.resources_influx.serialize()
        dictionary["type"] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.pos = dictionary["pos"]
        self.name = dictionary["name"]
        self.degradation = dictionary["degradation"]
        self.resources = Matter(dictionary["resources"])
        self.resources_influx = Matter(dictionary["resources_influx"])


if __name__ == "__main__":
    object = Market(
        name="Sample",
        pos=[0, 0],
        resources_influx={'food': 1, 'water': 1, 'energy': 1},
    )
    object.update(duration=10)
    print(object)
