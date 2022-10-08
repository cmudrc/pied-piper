import numpy as np


class Boundery:
    def __init__(self, center):
        self.center = center

    def is_in(self, other):
        return False


class Circular(Boundery):
    def __init__(self, center, radius):
        super().__init__(
            center=center
        )
        self.radius = radius

    def is_in(self, other):
        distance = self.distance_from_center(other)
        result = False
        if distance <= self.radius:
            result = True
        return result

    def distance_from_center(self, other):
        x_0 = self.center[0]
        y_0 = self.center[1]
        x_1 = other.pos[0]
        y_1 = other.pos[1]
        return np.power(np.power(x_0 - x_1, 2) + np.power(y_0 - y_1, 2), 0.5)


if __name__ == "__main__":
    class Other():
        def __init__(self, pos):
            self.pos = pos


    other = Other(pos=[1, 1])
    boundery = Circular(center=[0, 0], radius=2)
    print(boundery.is_in(other))
