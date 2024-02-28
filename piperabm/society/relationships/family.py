from piperabm.object import PureObject


class Family(PureObject):

    section = "society"
    category = "edge"
    type = "family"

    def __init__(
        self,
        id_1: int = None,
        id_2: int = None,
        home_id: int = None
    ):
        super().__init__()
        self.id_1 = id_1
        self.id_2 = id_2
        self.home_id = home_id
        self.name = ''
        self.id = None
        self.model = None

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['id_1'] = self.id_1
        dictionary['id_2'] = self.id_2
        dictionary['id'] = self.id
        dictionary['home_id'] = self.home_id
        dictionary["section"] = self.section
        dictionary["category"] = self.category
        dictionary["type"] = self.type
        return dictionary
    
    def deserialize(self, dictionary):
        if dictionary['type'] != self.type:
            raise ValueError
        self.id_1 = int(dictionary['id_1'])
        self.id_2 = int(dictionary['id_2'])
        self.home_id = int(dictionary['home_id'])
        

if __name__ == "__main__":
    family = Family(
        id_1=1,
        id_2=2,
        home_id=5
    )
    family.print()