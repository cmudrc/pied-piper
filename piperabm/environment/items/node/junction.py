from piperabm.object import Item


class Junction(Item):

    def __init__(
        self,
        pos: list = None,
        name: str = ''
    ):
        super().__init__(
            name=name
        )
        self.pos = pos
        self.category = "node"
        self.type = "junction"

    def serialize(self) -> dict:
        dictionary = super().serialize()
        dictionary["pos"] = self.pos
        dictionary["category"] = self.category
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        super().deserialize(dictionary)
        self.pos = dictionary["pos"]
        self.category = dictionary["category"]


if __name__ == "__main__":
    item = Junction(
        name="sample",
        pos=[0, 0]
    )
    item.print
