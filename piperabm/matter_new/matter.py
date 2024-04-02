from copy import deepcopy

from piperabm.object import PureObject
from piperabm.tools.symbols import SYMBOLS


class Matter(PureObject):

    def __init__(self, matter: dict = {}):
        super().__init__()
        for name in matter:
            if matter[name] < 0:
                raise ValueError
        self.library = matter

    @property
    def names(self):
        return self.library.keys()

    def check_empty(self, names: list = None):
        """
        Check whether any zero amount of a matter exists between names
        """
        results = []
        if names is None:
            names = self.names
        for name in names:
            if name in self.library:
                if self.library[name] < 0:
                    results.append(name)
            else:
                results.append(name)
        return results
        '''
        for name in names:
            if name in self.library:
                if self.library[name] > 0:
                    results.append(False)
                else:
                    results.append(True)
            else:
                results.append(True)
        if True in results:
            return True
        else:
            return False
        '''
        
    def values(self, prices):
        result = {}
        for name in prices:
            if name in self.library:
                result[name] = self.library[name] * prices[name]
        return result
    
    def value(self, prices):
        values = self.values(prices)
        total = 0
        for name in values:
            total += values[name]
        return total

    def from_value(self, values, prices):
        for name in values:
            if name in prices:
                self.library[name] = values[name] / prices[name]

    def __add__(self, other):
        other = deepcopy(other)
        if isinstance(other, dict):
            for name in other:
                if name not in self.library:
                    self.library[name] = 0
                self.library[name] += other[name]
                other[name] = 0
            return Matter(other)
        elif isinstance(other, Matter):
            return self.__add__(other.library)
        else:
            raise ValueError

    def __sub__(self, other):
        other = deepcopy(other)
        if isinstance(other, dict):
            for name in other:
                if name in self.library:
                    if self.library[name] >= other[name]:
                        self.library[name] -= other[name]
                        other[name] = 0
                    else:
                        other[name] -= self.library[name]
                        self.library[name] = 0
            return Matter(other)
        elif isinstance(other, Matter):
            return self.__sub__(other.library)
        else:
            raise ValueError
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            library = deepcopy(self.library)
            for name in library:
                library[name] *= other
            return Matter(library)
        elif isinstance(other, dict):
            library = deepcopy(self.library)
            for name in other:
                library[name] *= other[name]
            return Matter(library)
        else:
            raise ValueError
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            library = deepcopy(self.library)
            for name in library:
                library[name] /= other
            return Matter(library)
        elif isinstance(other, dict):
            library = deepcopy(self.library)
            for name in other:
                if other[name] == 0:
                    library[name] = SYMBOLS['inf']
                else:
                    library[name] /= other[name]
            return Matter(library)
        elif isinstance(other, Matter):
            other_library = deepcopy(other.library)
            return self.__truediv__(other_library)
        else:
            raise ValueError

    def serialize(self) -> dict:
        return self.library
    
    def deserialize(self, dictionary: dict) -> None:
        self.library = dictionary

    
if __name__ == "__main__":
    matter = Matter({"food": 2, "water": 2, "energy": 3})
    other = Matter({"food": 1})
    #print(matter, other)

    #remainder = matter - other
    #print(matter.has_zero())
    #print(matter, other, remainder)
    new_matter = matter / other
    print(new_matter)

