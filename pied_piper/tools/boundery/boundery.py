import numpy as np


class Boundery:
    """
    An enclosed area in space.
    """

    def __init__(self, center):
        """
        Args:
            center: position of center of boundery in [x, y] form.
        """
        self.center = center

    def is_in(self, other):
        return False


class Circular(Boundery):
    """
    A circular boundery in space.
    """
    
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

    def distance_from_boundery(self, other):
        return self.distance_from_center - self.radius


class Rectangular(Boundery):

    def __init__(self, center, width, height, theta=0):
        super().__init__(
            center=center
        )
        self.width = width
        self.height = height
        self.theta = theta
    
    def is_in(self, other):
        result = False
        x_0 = self.center[0]
        y_0 = self.center[1]
        x_1 = other.pos[0]
        y_1 = other.pos[1]
        rot_mat = np.array([[np.cos(self.theta), np.sin(self.theta)], [-np.sin(self.theta), np.cos(self.theta)]])
        pos_prime = np.matmul(rot_mat, np.array([x_1, y_1]))
        #print(pos_prime)
        x_1 = pos_prime[0]
        y_1 = pos_prime[1]
        #print((y_1 - y_0))
        #print((y_1 - y_0) <= self.height / 2)
        #print((y_1 - y_0) >= -self.height / 2)
        if (x_1 - x_0) <= self.width / 2 and \
            (x_1 - x_0) >= -self.width / 2:
            if (y_1 - y_0) <= self.height / 2 and \
                (y_1 - y_0) >= -self.height / 2:
                result = True
        return result


if __name__ == "__main__":
    class Other():
        def __init__(self, pos):
            self.pos = pos


    other = Other(pos=[1, 1])
    boundery = Circular(center=[0, 0], radius=2)
    #print(boundery.is_in(other))

    other = Other(pos=[0.7, 0.7])
    boundery = Rectangular(center=[0, 0], width=2, height=1, theta=0.3)
    print(boundery.is_in(other))
