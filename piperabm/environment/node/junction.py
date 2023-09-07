from piperabm.environment.node.object import Object


class Junction(Object):

    def __init__(
            self,
            id: str = '',
            name: str = '',
            pos: list = [0, 0]
        ):
        super().__init__(
            id=id,
            name=name,
            pos=pos
        )
        self.type = 'junction'
    
    def serialize(self) -> dict:
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['name'] = self.name
        dictionary['pos'] = self.pos


if __name__ == "__main__":
    node = Junction(
        id='1',
        name='square',
        pos=[0, 0]
    )