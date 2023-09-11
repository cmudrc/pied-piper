from piperabm.environment.node.junction import Junction
from piperabm.environment.degradation import Degradation
from piperabm.unit import Date


class Settlement(Junction):

    def __init__(
            self,
            id: str = '',
            name: str = '',
            pos: list = [0, 0],
            date_start: Date = Date.today(),
            date_end: Date = None,
            degradation = Degradation()
        ):
        super().__init__(
            id=id,
            name=name,
            pos=pos
        )
        self.date_start = date_start
        self.date_end = date_end
        self.degradation = degradation
        self.type = 'settlement'

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['name'] = self.name
        dictionary['pos'] = self.pos
        dictionary['date_start'] = '' #
        dictionary['date_end'] = '' #
        dictionary['degradation'] = '' #
        return dictionary


if __name__ == "__main__":
    node = Settlement(
        id='1',
        name='square',
        pos=[0, 0]
    )