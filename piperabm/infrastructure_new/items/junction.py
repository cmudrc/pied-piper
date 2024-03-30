from piperabm.object import PureObject


class Junction(PureObject):

    section = "infrastructure"
    category = "node"
    type = "junction"

    def __init__(
        self,
        pos: list = None,
        name: str = ""
    ):
        super().__init__()

        self.infrastructure = None  # Bind

        self.pos = pos
        self.name = name

    def serialize(self) -> dict:
        dictionary = {}
        dictionary["pos"] = self.pos
        dictionary["name"] = self.name
        dictionary["type"] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.pos = dictionary["pos"]
        self.name = dictionary["name"]


if __name__ == "__main__":
    object = Junction(
        name="Sample",
        pos=[0, 0]
    )
    print(object)
