from piperabm.object import PureObject
from piperabm.degradation import Degradation


class Settlement(PureObject):

    section = "infrastructure"
    category = "node"
    type = "settlement"

    def __init__(
        self,
        pos: list = None,
        name: str = "",
        degradation: Degradation = None,
        id: int = None
    ):
        super().__init__()
        
        self.model = None  # to access model

        self.pos = pos
        self.name = name
        if degradation is None:
            degradation = Degradation()
        self.degradation = degradation
        self.id = id

    def serialize(self) -> dict:
        dictionary = {}
        dictionary["pos"] = self.pos
        dictionary["name"] = self.name
        dictionary["degradation"] = self.degradation.serialize()
        dictionary["id"] = self.id
        dictionary["section"] = self.section
        dictionary["category"] = self.category
        dictionary["type"] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        self.pos = dictionary["pos"]
        self.name = dictionary["name"]
        self.degradation = Degradation()
        self.degradation.deserialize(dictionary["degradation"])
        self.id = int(dictionary["id"])


if __name__ == "__main__":
    object = Settlement(
        name="Sample",
        pos=[0, 0]
    )
    object.print()
