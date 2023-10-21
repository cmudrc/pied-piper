from piperabm.society.items.edge.relationship import Relationship


class Family(Relationship):

    def __init__(
        self,
        index_1: int = None,
        index_2: int = None,
        home_index: int = None
    ):
        super().__init__(
            index_1=index_1,
            index_2=index_2
        )
        self.home_index = home_index
        self.type = "family"

    def serialize(self) -> dict:
        dictionary = super().serialize()
        dictionary['home_index'] = self.home_index
        return dictionary
        

if __name__ == "__main__":
    family = Family(
        index_1=1,
        index_2=2,
        home_index=5
    )
    family.print