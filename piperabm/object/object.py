from pprint import pprint

from piperabm.tools.symbols import SYMBOLS
from piperabm.object.delta import Delta


class Object:
    """
    Pure object for the model
    """

    def __init__(self):
        self.type = 'pure object'

    def print(self):
        pprint(self.to_dict())

    def __str__(self) -> str:
        return str(self.to_dict())

    def __eq__(self, other) -> bool:
        result = False
        if self.to_dict() == other.to_dict():
            result = True
        return result
    
    def to_dict(self) -> dict:
        dictionary = {}
        print("NOT IMPLEMENTED YET")
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        print("NOT IMPLEMENTED YET")

    '''
    def add_delta(self, delta: dict) -> None:
        dictionary = self.to_dict()
        for key in delta:
            dictionary[key] += delta[key]
        self.from_dict(dictionary)
    '''
        
    def __add__(self, other) -> None:
        if isinstance(other, dict):
            dictionary = self.to_dict()
            dictionary_new = Delta.apply_delta(dictionary, other)
            self.from_dict(dictionary_new)
            '''
            for key in other:
                if hasattr(self, key):
                    attr = getattr(self, key)
                    attr += other[key]
                    setattr(self, key, attr)
            '''

    def __sub__(self, other) -> None:
        if not isinstance(other, dict):
            other = other.to_dict()
        dictionary = self.to_dict()
        delta = Delta.create_delta(dictionary, other)
        return delta

        '''
        for key in other_dict:
            if hasattr(self, key):
                attr = getattr(self, key)
                attr -= other_dict[key]
                setattr(self, key, attr)  
        '''     

    def __mul__(self, other) -> None:
        if isinstance(other, dict):
            for key in other:
                if hasattr(self, key):
                    attr = getattr(self, key)
                    attr *= other[key]
                    setattr(self, key, attr)

    def __truediv__(self, other) -> None:
        if isinstance(other, dict):
            for key in other:
                if hasattr(self, key):
                    attr = getattr(self, key)
                    other_val = other[key]
                    if abs(other_val) < SYMBOLS['eps']:
                        attr = SYMBOLS['inf']
                    else:
                        attr /= other[key]
                    setattr(self, key, attr)