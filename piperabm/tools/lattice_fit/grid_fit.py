import numpy as np


class GridFit:

    def __init__(self, data):
        self.data = np.array(data)

    @property
    def len(self):
        return len(self.data)
    
    def generate_grid(self, start, step):
        count = self.len
        end = start + (count - 1) * step
        return np.linspace(start, end, count)
    
    def RMSE(self, grid):
        return np.sqrt(np.square(self.data - grid).mean())
    
    def solve(self, start_min, start_max, start_count, step_min, step_max):
        pass



if __name__ == "__main__":
    data = [0, 1.1, 1.9, 3.1, 3.9]
    gd = GridFit(data)
    grid = gd.generate_grid(0, 1)
    print(gd.RMSE(grid))