import numpy as np


class GridFit:

    def __init__(self, numbers):
        self.numbers = np.array(numbers)

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

    @property
    def guess_grid_size(self):
        distances = []
        for index in range(self.len):
            if index != 0 and \
            index != self.len - 1:
                nearest_distances = self.nearest_neighbors_distances(index)
                mean_distance = sum(nearest_distances) / 2
                distances.append(mean_distance)
        return sum(distances) / len(distances)

    def distances(self, input_index):
        distances = []
        input_value = self.get(input_index)
        for index, number in enumerate(self.numbers):
            distance = abs(number - input_value)
            distances.append([distance, index])
        distances = [[distance, index]
                            for distance, index in sorted(distances)]
        return distances
    
    def nearest_neighbors(self, input_index, neighbors=2):
        distances = self.distances(input_index)
        start = 1
        return distances[start:start+neighbors]
    
    def nearest_neighbors_distances(self, input_index, neighbors=2):
        distances = self.nearest_neighbors(input_index, neighbors=2)
        return [distance for distance, index in distances]
    
    def generate_grid(self, start, step):
        count = self.len
        end = start + (count - 1) * step
        return np.linspace(start, end, count)
    
    def RMSE(self, grid):
        return np.sqrt(np.square(self.numbers - grid).mean())
    
    def solve(self, start_min, start_max, start_count, step_min, step_max):
        pass



if __name__ == "__main__":
    numbers = [0, 1.1, 1.9, 3.1, 3.9]
    grid = GridFit(numbers)
    print(grid.guess_grid_size)