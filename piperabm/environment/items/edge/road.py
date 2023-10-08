from piperabm.object import Item
from piperabm.environment.items.degradation import Degradation
from piperabm.time import Date
from piperabm.tools.coordinate.distance import distance_point_to_point


class Road(Item):

    def __init__(
        self,
        pos_1: list = None,
        pos_2: list = None,
        name: str = '',
        date_start: Date = None,
        date_end: Date = None,
        length_actual: float = None,
        roughness: float = 1,
        degradation=Degradation()
    ):
        super().__init__(
            name=name,
            date_start=date_start,
            date_end=date_end
        )
        self.environment = None  # to access environment information
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.length_actual = length_actual
        self.roughness = roughness
        self.degradation = degradation
        self.category = "edge"
        self.type = "road"

    @property
    def length_linear(self):
        """
        Eucledian distance between two ends of the edge
        """
        result = None
        if self.pos_1 is not None and self.pos_2 is not None:
            result = distance_point_to_point(self.pos_1, self.pos_2)
        return result

    @property
    def length(self):
        """
        Compare and return the most appropriate definition of length
        """
        result = None
        linear = self.length_linear
        actual = self.length_actual
        if linear is not None:
            if actual is not None:
                if actual > linear:
                    result = actual
                else:
                    result = linear
            else:  # when *actual* is None
                result = linear
        else:
            if actual is not None:
                result = actual
        return result
    
    @property
    def adjusted_length(self):
        return self.length * self.roughness * self.degradation.factor

    def serialize(self) -> dict:
        dictionary = super().serialize()
        dictionary["pos_1"] = self.pos_1
        dictionary["pos_2"] = self.pos_2
        dictionary["length_actual"] = self.length_actual
        dictionary["roughness"] = self.roughness
        dictionary["degradation"] = self.degradation.serialize()
        dictionary["category"] = self.category
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        super().deserialize(dictionary)
        self.pos_1 = dictionary["pos_1"]
        self.pos_2 = dictionary["pos_2"]
        self.length_actual = dictionary["length_actual"]
        self.roughness = dictionary["roughness"]
        self.degradation = Degradation().deserialize(dictionary["degradation"])
        self.category = dictionary["category"]


if __name__ == "__main__":
    item = Road(
        name="road"
    )
    item.print
