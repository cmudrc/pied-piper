from piperabm.object import PureObject
#from uuid import SafeUUID


class Object(PureObject):
    """ Object for node items in environment graph """

    def __init__(
        self,
        id: str = '',
        name: str = '',
        pos: list = [0, 0]
    ):
        self.id = id
        self.name = name
        self.pos = pos
        self.category = 'node'
        self.type = 'object'    


if __name__ == '__main__':
    node = Object(
        id='1',
        name='sample',
        pos=[0, 0],
    )