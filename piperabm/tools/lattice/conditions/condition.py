import numpy as np


class Condition:

    def __init__(self, name, filter):
        self.name = name
        self.create_filters(filter)

    def create_filters(self, filter):
        self.filters = []
        filter = np.array(filter)
        self.filters.append(filter)
        for _ in range(3):
            filter = np.rot90(self.filters[-1])
            if self.filter_exists(filter) is False:
                self.filters.append(filter)

    def filter_exists(self, new_filter):
        result = False
        for filter in self.filters:
            comparison = filter == new_filter
            if comparison.all() == True:
                result = True
                break
        return result
    
    def check(self, input):
        result = False
        for filter in self.filters:
            comparison = filter == input
            if comparison.all() == True:
                result = True
                break
        return result
    

if __name__ == '__main__':
    filter = [
        [0, 0, 0,],
        [1, 1, 1,],
        [0, 1, 0,],
    ]
    
    c1 = Condition(
        name="T",
        filter=filter
    )
    print(c1.filters)
