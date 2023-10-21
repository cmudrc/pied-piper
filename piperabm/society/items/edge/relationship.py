from piperabm.object import PureObject


class Relationship(PureObject):

    def __init__(
        self,
        index_1: int = None,
        index_2: int = None
    ):
        self.index_1 = index_1
        self.index_2 = index_2
        self.type = "relationship"

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['index_1'] = self.index_1
        dictionary['index_2'] = self.index_2
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        self.index_1 = dictionary['index_1']
        self.index_2 = dictionary['index_2']
        self.type = dictionary['type']


if __name__ == "__main__":
    relationship = Relationship(
        index_1=1,
        index_2=2
    )
    relationship.print