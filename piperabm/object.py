from pprint import pprint

from piperabm.tools.symbols import SYMBOLS


class Object:
    """
    Pure object for the model
    """

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

    def __add__(self, other) -> None:
        if isinstance(other, dict):
            for key in other:
                if hasattr(self, key):
                    attr = getattr(self, key)
                    attr += other[key]
                    setattr(self, key, attr)

    def __sub__(self, other) -> None:
        if isinstance(other, dict):
            for key in other:
                if hasattr(self, key):
                    attr = getattr(self, key)
                    attr -= other[key]
                    setattr(self, key, attr)       

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