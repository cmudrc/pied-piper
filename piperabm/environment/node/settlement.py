from piperabm.environment.node.object import Object


class Settlement(Object):

    def __init__(
            self,
            id: int,
            name: str = '',
            pos: list = [0, 0],
            degradation = None
        ):
        super().__init__(
            id=id,
            name=name,
            pos=pos,
            degradation=degradation
        )
        self.type = 'settlement'


if __name__ == "__main__":
    settlement = Settlement(
        id=1,
        name='square',
        pos=[0, 0],
        degradation=None
    )