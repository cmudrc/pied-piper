from piperabm.object import PureObject
from piperabm.tools.coordinate import distance as ds
from piperabm.infrastructure_new.degradation import degradation_function


class Street(PureObject):

    section = "infrastructure"
    category = "edge"
    type = "street"

    def __init__(
        self,
        pos_1: list = None,
        pos_2: list = None,
        name: str = "",
        difficulty: float = 1,
        degradation: float = 0,
    ):
        super().__init__()
        
        self.infrastructure = None  # to access model

        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.name = name
        self.difficulty = difficulty
        self.degradation = degradation

    @property
    def length(self):
        """
        Eucledian distance between two ends of the edge
        """
        result = None
        if self.pos_1 is not None and self.pos_2 is not None:
            result = ds.point_to_point(self.pos_1, self.pos_2)
        return result
    
    @property
    def adjusted_length(self):
        """
        Calculate adjusted length based on physical length, difficulty, and degradation factor
        """
        return self.length * self.difficulty * degradation_function(self.degradation)

    def serialize(self) -> dict:
        dictionary = {}
        dictionary["pos_1"] = self.pos_1
        dictionary["pos_2"] = self.pos_2
        dictionary["name"] = self.name
        dictionary["difficulty"] = self.difficulty
        dictionary["degradation"] = self.degradation
        dictionary["type"] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.pos_1 = dictionary["pos_1"]
        self.pos_2 = dictionary["pos_2"]
        self.name = dictionary["name"]
        self.difficulty = dictionary["difficulty"]
        self.degradation = dictionary["degradation"]


if __name__ == "__main__":
    object = Street(
        pos_1=[0, 0],
        pos_2=[3, 4],
        name="Sample"
    )
    print(object)