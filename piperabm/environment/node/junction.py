from piperabm.environment.node.object import Object


class Junction(Object):

    def __init__(
            self,
            id: int,
            name: str = '',
            pos: list = [0, 0]
        ):
        super().__init__(
            id=id,
            name=name,
            pos=pos
        )
        self.type = 'junction'


if __name__ == "__main__":
    junction = Junction(
        id=1,
        name='square',
        pos=[0, 0]
    )