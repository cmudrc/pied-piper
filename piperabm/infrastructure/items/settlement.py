from piperabm.object import PureObject
from piperabm.degradation import Degradation


class Settlement(PureObject):

    def __init__(
        self,
        pos: list = None,
        name: str = "",
        degradation=Degradation()
    ):
        super().__init__()
        
        self.model = None  # to access model

        self.pos = pos
        self.name = name
        self.degradation = degradation

        self.section = "infrastructure"
        self.category = "node"
        self.type = "settlement"

    def serialize(self) -> dict:
        dictionary = {}
        dictionary["pos"] = self.pos
        dictionary["name"] = self.name
        dictionary["degradation"] = self.degradation.serialize()
        dictionary["category"] = self.category
        dictionary["type"] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.pos = dictionary["pos"]
        self.name = dictionary["name"]
        self.degradation = Degradation()
        self.degradation.deserialize(dictionary["degradation"])
        self.category = dictionary["category"]
        self.type = dictionary["type"]


if __name__ == "__main__":
    item = Settlement(
        name='sample',
        pos=[0, 0]
    )
    item.print
