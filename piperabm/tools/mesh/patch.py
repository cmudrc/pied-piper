import random

from piperabm.tools.mesh.triangle import Triangle


class Patch:

    def __init__(self):
        self.library = []

    def add(self, *triangles):
        for triangle in triangles:
            if isinstance(triangle, Triangle):
                self.library.append(triangle)

    @property
    def weights(self):
        result = []
        for triangle in self.library:
            result.append(triangle.weight)
        return result
    
    @property
    def indexes(self):
        result = []
        for i in range(len(self.library)):
            result.append(i)
        return result
    
    def random_point(self):
        values = self.indexes
        weights = self.weights
        index = random.choices(values, weights=weights, k=1)[0]
        triangle = self.library[index]
        return triangle.random_point()


if __name__ == "__main__":
    pos_1 = [0, 0]
    pos_2 = [0, 2]
    pos_3 = [2, 0]
    pos_4 = [1, 1]
    pos_5 = [2, 1]
    triangle_1 = Triangle(pos_1, pos_2, pos_3)
    triangle_2 = Triangle(pos_3, pos_4, pos_5)

    patch = Patch()
    patch.add(triangle_1, triangle_2)

    print(patch.weights)