from piperabm.object import PureObject


class Junction(PureObject):

    def __init__(
        self,
        name: str = '',
        pos: list = [0, 0]
    ):
        self.index = None
        self.name = name
        self.pos = pos
        self.type = 'junction'

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['index'] = self.index
        dictionary['name'] = self.name
        dictionary['pos'] = self.pos
        return dictionary


if __name__ == "__main__":
    item = Junction(
        name='sample',
        pos=[0, 0]
    )
    print(item)
