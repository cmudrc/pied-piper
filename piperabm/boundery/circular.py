from random import uniform
import matplotlib.pyplot as plt

try:
    from .boundery_super import Boundery
except:
    from boundery_super import Boundery


class Circular(Boundery):
    """
    Create a circular boundery in space.
    """

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def is_in(self, other):
        distance = self._distance_from_center(other)
        result = False
        if distance <= self.radius:
            result = True
        return result

    def _distance_from_boundery(self, other):
        return self._distance_from_center - self.radius

    def rand_pos(self) -> list:
        result = None
        while True:
            pos = [uniform(-self.radius, self.radius),
                   uniform(-self.radius, self.radius)]
            if self.is_in(pos):
                result = pos
                break
        return list(result)

    def to_dict(self) -> dict:
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

    def xylim(self):
        xlim = [-2*self.radius + self.center[0],
                2*self.radius + self.center[0]]
        ylim = [-2*self.radius + self.center[1],
                2*self.radius + self.center[1]]
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
    circular = Circular(radius=1.5)
    circular.center = [-2, -2]
    circular.show()
