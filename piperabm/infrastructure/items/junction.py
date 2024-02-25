from piperabm.object import PureObject


class Junction(PureObject):

    section = 'infrastructure'
    category = 'node'
    type = 'junction'

    def __init__(
        self,
        pos: list = None,
        name: str = '',
        id: int = None
    ):
        super().__init__()

        self.model = None  # to access model

        self.pos = pos
        self.name = name
        self.id = id

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['pos'] = self.pos
        dictionary['name'] = self.name
        dictionary['id'] = self.id
        dictionary['section'] = self.section
        dictionary['category'] = self.category
        dictionary['type'] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.pos = dictionary['pos']
        self.name = dictionary['name']
        self.id = int(dictionary['id'])
        self.section = dictionary['section']
        self.category = dictionary['category']
        self.type = dictionary['type']


if __name__ == '__main__':
    object = Junction(
        name='Sample',
        pos=[0, 0]
    )
    object.print()
