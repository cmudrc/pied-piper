from piperabm.object import PureObject


class Junction(PureObject):

    section = 'infrastructure'
    category = 'node'
    type = 'junction'

    def __init__(
        self,
        pos: list = None,
        name: str = ''
    ):
        super().__init__()

        self.model = None  # to access model

        self.pos = pos
        self.name = name

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['pos'] = self.pos
        dictionary['name'] = self.name
        dictionary['section'] = self.section
        dictionary['category'] = self.category
        dictionary['type'] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.pos = dictionary['pos']
        self.name = dictionary['name']
        self.section = dictionary['section']
        self.category = dictionary['category']
        self.type = dictionary['type']


if __name__ == '__main__':
    item = Junction(
        name='Sample',
        pos=[0, 0]
    )
    item.print
