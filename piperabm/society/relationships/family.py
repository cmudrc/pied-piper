from piperabm.object import PureObject


class Family(PureObject):

    def __init__(
        self,
        index_1: int = None,
        index_2: int = None,
        home_index: int = None
    ):
        super().__init__()
        self.index_1 = index_1
        self.index_2 = index_2
        self.home_index = home_index
        self.type = "family"

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['index_1'] = self.index_1
        dictionary['index_2'] = self.index_2
        dictionary['home_index'] = self.home_index
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary):
        self.index_1 = dictionary['index_1']
        self.index_2 = dictionary['index_2']
        self.home_index = dictionary['home_index']
        self.type = dictionary['type']
        

if __name__ == "__main__":
    family = Family(
        index_1=1,
        index_2=2,
        home_index=5
    )
    family.print