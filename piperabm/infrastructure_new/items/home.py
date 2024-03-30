from piperabm.object import PureObject
from piperabm.degradation import Degradation


class Home(PureObject):

    section = "infrastructure"
    category = "node"
    type = "home"

    def __init__(
        self,
        pos: list = None,
        name: str = "",
        degradation: float = 0,
    ):
        super().__init__()
        
        self.infrastructure = None  # to access model

        self.pos = pos
        self.name = name
        self.degradation = degradation

    def serialize(self) -> dict:
        dictionary = {}
        dictionary["pos"] = self.pos
        dictionary["name"] = self.name
        dictionary["degradation"] = self.degradation
        dictionary["type"] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.pos = dictionary["pos"]
        self.name = dictionary["name"]
        self.degradation = dictionary["degradation"]


if __name__ == "__main__":
    object = Home(
        name="Sample",
        pos=[0, 0]
    )
    print(object)
