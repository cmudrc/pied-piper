import random

from piperabm.tools.mesh.triangle import Triangle


class Patch:
    """
    A group of triangles create a patch.
    """

    def __init__(self):
        self.library = []

    def add(self, *triangles):
        """
        Add new triangle objects to the patch.
        """
        for triangle in triangles:
            if isinstance(triangle, Triangle):
                self.library.append(triangle)

    @property
    def weights(self) -> list:
        """
        Return a list of weights oeganized by triangle orders.
        """
        result = []
        for triangle in self.library:
            result.append(triangle.weight)
        return result

    @property
    def indexes(self) -> list:
        """
        Return the list of triangle indexes.
        """
        result = []
        for i in range(len(self.library)):
            result.append(i)
        return result

    def random_point(self):
        """
        Generate a random point inside the patch based on the weights.
        """
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
