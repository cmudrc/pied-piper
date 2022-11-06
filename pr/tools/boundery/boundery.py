import numpy as np
#import matplotlib.pyplot as plt
from random import uniform, seed

from pr.graphics.plt.boundery import circular_boundery_to_plt, rectangular_boundery_to_plt


class Boundery:
    """
    Define an enclosed area in space.
    """

    def __init__(self, center):
        """
        Args:
            center: position of center of boundery in [x, y] form.
        """
        self.center = center

    def is_in(self, other):
        """
        Check the other to see whether it is located inside the boundery or not.
        """
        return False

    def _distance_from_center(self, other):
        """
        Calculate the distance from center.
        """
        x_0 = self.center[0]
        y_0 = self.center[1]
        if isinstance(other, list):
            x_1 = other[0]
            y_1 = other[1]
        else:
            x_1 = other.pos[0]
            y_1 = other.pos[1]
        return np.power(np.power(x_0 - x_1, 2) + np.power(y_0 - y_1, 2), 0.5)

    def _distance_from_boundery(self, other):
        """
        Calculate the distance from boundery.
        """
        return None
    
    def distance(self, other, mode='center'):
        """
        Calculate the distance.
        """
        if mode == 'center':
            return self._distance_from_center(other)
        elif mode == 'boundery':
            return self._distance_from_boundery(other)

    def add_patch(self, color='blue'):
        """
        Add the boundery to plt graph
        """
        pass
    

class Circular(Boundery):
    """
    Create a circular boundery in space.
    """
    
    def __init__(self, center, radius):
        super().__init__(
            center=center
        )
        self.radius = radius

    def is_in(self, other):
        distance = self._distance_from_center(other)
        result = False
        if distance <= self.radius:
            result = True
        return result

    def _distance_from_boundery(self, other):
        return self._distance_from_center - self.radius

    def rand_pos(self):
        result = None
        while True:
            pos = [uniform(-self.radius, self.radius), uniform(-self.radius, self.radius)]
            if self.is_in(pos):
                result = pos
                break
        return list(result)

    def to_dict(self):
        dictionary = {
            'type': 'circular',
            'center': self.center,
            'radius': self.radius,
        }
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        self.center = d['center']
        self.radius = d['radius']

    def to_plt(self):
        circular_boundery_to_plt(self.to_dict())


class Rectangular(Boundery):
    """
    Create a rectangular boundery in space.
    """

    def __init__(self, center, width, height, theta=0):
        super().__init__(
            center=center
        )
        self.width = width # (x_max - x_min)
        self.height = height # (y_max - y_min)
        self.theta = theta
    
    def is_in(self, other):
        result = False
        x_0 = self.center[0]
        y_0 = self.center[1]
        rot_mat = np.array([[np.cos(self.theta), np.sin(self.theta)], [-np.sin(self.theta), np.cos(self.theta)]])
        if isinstance(other, list):
            other_pos = other
        else:
            other_pos = other.pos
        pos_prime = np.matmul(rot_mat, np.array(other_pos))
        x_1 = pos_prime[0]
        y_1 = pos_prime[1]
        if (x_1 - x_0) <= self.width / 2 and \
            (x_1 - x_0) >= -self.width / 2:
            if (y_1 - y_0) <= self.height / 2 and \
                (y_1 - y_0) >= -self.height / 2:
                result = True
        return result

    def _distance_from_boundery(self, other):
        distance = 0
        if not self.is_in(other):
            distance_from_center = self._distance_from_center(other)
            x_0 = self.center[0]
            y_0 = self.center[1]
            rot_mat = np.array([[np.cos(self.theta), np.sin(self.theta)], [-np.sin(self.theta), np.cos(self.theta)]])
            if isinstance(other, list):
                other_pos = other
            else:
                other_pos = other.pos
            pos_prime = np.matmul(rot_mat, np.array(other_pos))
            x_1 = np.abs(pos_prime[0])
            y_1 = np.abs(pos_prime[1])
            slope = (y_1 - y_0) / (x_1 - x_0)
            if slope <= self.height / self.width:
                slope_theta = np.arctan(slope)
                center_to_boundery = (self.width / 2) / np.cos(slope_theta)
            else:
                slope_theta = np.arctan(slope)
                center_to_boundery = (self.height / 2) / np.sin(slope_theta)
            distance = distance_from_center - center_to_boundery
        return distance

    def rand_pos(self):
        pos = [uniform(-self.width/2, self.width/2), uniform(-self.height/2, self.height/2)]
        rot_mat = np.array([[np.cos(self.theta), -np.sin(self.theta)], [np.sin(self.theta), np.cos(self.theta)]])
        result = np.matmul(rot_mat, np.array(pos))
        return list(result)

    def to_dict(self):
        dictionary = {
            'type': 'rectangular',
            'center': self.center,
            'width': self.width,
            'height': self.height,
            'theta': self.theta,
        }
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        self.center = d['center']
        self.width = d['width']
        self.height = d['height']
        self.theta = d['theta']

    def to_plt(self):
        rectangular_boundery_to_plt(self.to_dict())


if __name__ == "__main__":
    class Other():
        def __init__(self, pos):
            self.pos = pos

    #other = Other(pos=[1, 1])
    #boundery = Circular(center=[0, 0], radius=2)
    #print(boundery.rand_pos())
    #print(boundery.is_in(other))

    other = Other(pos=[0.7, 0.7])
    boundery = Rectangular(center=[0, 0], width=2, height=1, theta=0.3)
    #print(boundery.rand_pos())
    #print(boundery.is_in(other))



    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    boundery.to_plt()
    plt.show()
