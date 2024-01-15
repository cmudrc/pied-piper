import numpy as np
import matplotlib.pyplot as plt


class HarmonicFit:

    def __init__(self, f_ratio, threshold=0.01):
        self.f1 = 1
        self.f2 = self.f1 * f_ratio
        self.threshold = threshold
        self.set_1 = [0, self.f1]
        self.set_2 = [0, self.f2]
        self.create_set()

    def RMSE(self, grid):
        return np.sqrt(np.square(self.data - grid).mean())
    
    def create_set(self):
        while True:
            last_item_1 = self.set_1[-1] 
            last_item_2 = self.set_2[-1]
            distance = np.abs(last_item_2 - last_item_1)
            if distance < self.threshold:
                break
            else:
                if last_item_2 > last_item_1:
                    new = last_item_1 + self.f1
                    self.set_1.append(new)
                else:
                    new = last_item_2 + self.f2
                    self.set_2.append(new)
        
    def nearest(self, input, set):
        nearest_distance = None
        nearest_val = None
        for val in set:
            distance = np.abs(input - val)
            if nearest_distance is None or distance < nearest_distance:
                nearest_val = val
                nearest_distance =  distance
        return nearest_val, nearest_distance
    
    @property
    def score(self):
        scores = []
        for val_2 in self.set_2:
            val, distance = self.nearest(val_2, self.set_1)
            scores.append(np.abs(distance))
        return np.sum(scores) / len(scores)


xpoints = np.linspace(1, 2, 10000)
ypoints = []
for x in xpoints:
    hf = HarmonicFit(x)
    y = hf.score
    ypoints.append(y)
ypoints = np.array(ypoints)

plt.plot(xpoints, ypoints)
plt.show()

