from piperabm.object import PureObject
from piperabm.environment.items.degradation import Degradation
from piperabm.time import Date, date_serialize


class Settlement(PureObject):

    def __init__(
            self,
            name: str = '',
            pos: list = [0, 0],
            date_start: Date = Date.today(),
            date_end: Date = None,
            degradation = Degradation()
        ):
        self.index = None
        self.name = name
        self.pos = pos
        self.date_start = date_start
        self.date_end = date_end
        self.degradation = degradation
        self.category = 'node'
        self.type = 'settlement'

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['index'] = self.index
        dictionary['name'] = self.name
        dictionary['pos'] = self.pos
        dictionary['date_start'] = date_serialize(self.date_start)
        dictionary['date_end'] = date_serialize(self.date_end)
        dictionary['degradation'] = self.degradation.serialize
        dictionary['category'] = self.category
        dictionary['type'] = self.type
        return dictionary


if __name__ == "__main__":
    item = Settlement(
        name='sample',
        pos=[0, 0]
    )
    print(item)