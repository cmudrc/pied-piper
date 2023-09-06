#from piperabm.object import PureObject
from piperabm.environment.degradation import Degradation
from piperabm.unit import Date
#from uuid import SafeUUID


class Object:

    def __init__(
        self,
        id: int,
        name: str = '',
        pos: list = [0, 0],
        date_start: Date = Date.today(),
        date_end: Date = None,
        degradation: Degradation = Degradation()
    ):
        self.id = id
        self.name = name
        self.pos = pos
        self.date_start = date_start
        self.date_end = date_end
        self.degradation = degradation
        self.type = 'node_object'


if __name__ == '__main__':
    object = Object(
        name='sample',
        pos=[0, 0],
    )
