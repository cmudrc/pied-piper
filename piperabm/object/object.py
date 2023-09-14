from pprint import pprint

from piperabm.tools.symbols import SYMBOLS
from piperabm.object.delta import Delta


class PureObject:
    """
    Pure object for the model
    """

    def __init__(self):
        self.type = 'pure object'

    @property
    def print(self):
        """ pretty print object """
        pprint(self.__str__())

    def __str__(self) -> str:
        """ show serialized format of object """
        return str(self.serialize())

    def __eq__(self, other) -> bool:
        """ Check equality for two objects """
        result = False
        if self.serialize() == other.serialize() and \
            self.serialize != {}:
            result = True
        return result
    
    def serialize(self) -> dict:
        """ Serialize object into a dictionary """
        dictionary = {}
        print("NOT IMPLEMENTED YET")
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        """ Load object from a dictionary """
        print("NOT IMPLEMENTED YET")

    def create_delta(self, other) -> dict:
        """ Create delta between object and *other* """
        if not isinstance(other, dict):
            other = other.serialize()
        dictionary = self.serialize()
        delta = Delta.create(other, dictionary)
        return delta

    def apply_delta(self, delta: dict) -> None:
        """ Apply delta for the object """
        dictionary = self.serialize()
        dictionary_new = Delta.apply(dictionary, delta)
        self.deserialize(dictionary_new)


if __name__ == '__main__':
    
    class Sample(PureObject):

        def __init__(self, value):
            super().__init__()
            self.value = value

        def serialize(self) -> dict:
            return {'value': self.value}
        
        def deserialize(self, dictionary: dict) -> None:
            self.value = dictionary['value']
        
    s_1 = Sample(value=1)
    s_2 = Sample(value=2)
    delta = s_2.create_delta(s_1)
    print(delta)
    s_1.apply_delta(delta)
    s_1.print
