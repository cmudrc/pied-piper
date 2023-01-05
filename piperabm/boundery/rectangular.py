import numpy as np
from random import uniform
import matplotlib.pyplot as plt

try:
    from .boundery_super import Boundery
except:
    from boundery_super import Boundery


class Rectangular(Boundery):
    """
    Create a rectangular boundery in space.
    """

    def __init__(self, width, height, theta=0):
        super().__init__()
        self.width = width  # (x_max - x_min)
        self.height = height  # (y_max - y_min)
        self.theta = theta

    def is_in(self, other):
        result = False
        x_0 = self.center[0]
        y_0 = self.center[1]
        rot_mat = np.array([[np.cos(self.theta), np.sin(
            self.theta)], [-np.sin(self.theta), np.cos(self.theta)]])
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
            rot_mat = np.array([[np.cos(self.theta), np.sin(
                self.theta)], [-np.sin(self.theta), np.cos(self.theta)]])
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

    def rand_pos(self) -> list:
        pos = [uniform(-self.width/2, self.width/2),
               uniform(-self.height/2, self.height/2)]
        rot_mat = np.array([[np.cos(self.theta), -np.sin(self.theta)],
                           [np.sin(self.theta), np.cos(self.theta)]])
        result = np.matmul(rot_mat, np.array(pos))
        return list(result)

    def to_dict(self) -> dict:
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

    def xylim(self):
        max_size = max(self.height, self.width)
        max_size *= 1.5
        xlim = [-max_size/2 + self.center[0], max_size/2 + self.center[0]]
        ylim = [-max_size/2 + self.center[1], max_size/2 + self.center[1]]
        return xlim, ylim

    def show(self, active=True):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis('equal')
        xlim, ylim = self.xylim()
        plt.xlim(xlim)
        plt.ylim(ylim)
        self.to_plt(ax, active)
        plt.show()


if __name__ == "__main__":
    rectangular = Rectangular(width=2, height=1, theta=0.3)
    rectangular.center = [0, 0]
    rectangular.show()
