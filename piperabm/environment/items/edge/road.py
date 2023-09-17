from piperabm.object import PureObject
from piperabm.environment.items.degradation import Degradation
from piperabm.time import Date, date_serialize
from piperabm.tools.coordinate.distance import distance_point_to_point


class Road(PureObject):

    def __init__(
            self,
            pos_1: list,
            pos_2: list,
            name: str = '',
            date_start: Date = Date.today(),
            date_end: Date = None,
            length_actual: float = None,
            roughness: float = 1,
            degradation = Degradation()
        ):
        self.environment = None  # to access environment information
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.name = name
        self.date_start = date_start
        self.date_end = date_end
        self.length_actual = length_actual
        self.roughness = roughness
        self.degradation = degradation
        self.category = 'edge'
        self.type = 'road'

    def find_index(self):
        if self.environment is not None:
            pass
    
    @property
    def length_linear(self):
        """ Eucledian distance between two ends of the edge """
        result = None
        if self.environment is not None:
            result = distance_point_to_point(self.pos_1, self.pos_2)
        return result
    
    @property
    def length(self):
        """ Compare and return the most appropriate definition of length """
        result = None
        linear = self.length_linear
        actual = self.length_actual
        if linear is not None:
            if actual is not None:
                if actual > linear:
                    result = actual
                else:
                    result = linear
            else:  # when actual is None
                result = linear
        else:
            if actual is not None:
                result = actual
        return result
    
    def serialize(self) -> dict:
        dictionary = {}
        dictionary['pos_1'] = self.pos_1
        dictionary['pos_2'] = self.pos_2
        dictionary['name'] = self.name
        dictionary['date_start'] = date_serialize(self.date_start)
        dictionary['date_end'] = date_serialize(self.date_end)
        dictionary['length_actual'] = self.length_actual
        dictionary['roughness'] = self.roughness
        dictionary['degradation'] = self.degradation.serialize()
        dictionary['category'] = self.category
        dictionary['type'] = self.type
        return dictionary


if __name__ == "__main__":
    item = Road(
        name='road'
    )
    print(item)