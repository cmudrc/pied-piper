import numpy as np


class GridFit:

    def __init__(self, numbers):
        self.numbers = numbers

    def get(self, index):
        return self.numbers[index]

    @property
    def min(self):
        return min(self.numbers)
    
    @property
    def max(self):
        return max(self.numbers)
    
    @property
    def len(self):
        return len(self.numbers)

    def grid_values(self, grid_start, grid_size):
        result = []
        min = self.min
        if grid_start > min:
            raise ValueError
        max = self.max
        value = grid_start
        while value < max:
            result.append(value)
            value += grid_size
        result.append(value)
        return result
    
    def score(self, grid):
        pass

    def find_nearest(self, value, grid):
        nearest_grid_value = None
        nearest_grid_distance = None
        for grid_value in grid:
            distance = np.abs(grid_value - value)
            if nearest_grid_distance is None or \
            nearest_grid_distance < distance:
                nearest_grid_distance = distance
                nearest_grid_value = grid_value
        return nearest_grid_value


if __name__ == "__main__":
    numbers = [1, 1.9, 3.1, 3.9]
    g = GridFit(numbers)
    r = g.grid_values(0, 0.9)
    print(r)