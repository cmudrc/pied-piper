from piperabm.object import Item
from piperabm.environment.items.degradation import Degradation
from piperabm.time import Date


class Settlement(Item):

    def __init__(
            self,
            pos: list = None,
            name: str = '',
            date_start: Date = None,
            date_end: Date = None,
            degradation = Degradation()
        ):
        super().__init__(
            name=name,
            date_start=date_start,
            date_end=date_end
        )
        self.pos = pos
        self.date_start = date_start
        self.date_end = date_end
        self.degradation = degradation
        self.category = "node"
        self.type = "settlement"

    def serialize(self) -> dict:
        dictionary = super().serialize()
        dictionary["pos"] = self.pos
        dictionary["degradation"] = self.degradation.serialize()
        dictionary["category"] = self.category
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        super().deserialize(dictionary)
        self.pos = dictionary["pos"]
        self.degradation = Degradation().deserialize(dictionary["degradation"])
        self.category = dictionary["category"]


if __name__ == "__main__":
    item = Settlement(
        name='sample',
        pos=[0, 0]
    )
    item.print