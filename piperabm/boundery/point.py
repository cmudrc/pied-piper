import matplotlib.pyplot as plt

try:
    from .circular import Circular
except:
    from circular import Circular


class Point(Circular):
    """
    Create a infitesimal circular boundery in space
    """

    def __init__(self):
        super().__init__(
            radius=0
        )

    def rand_pos(self) -> list:
        return self.center

    def to_dict(self) -> dict:
        dictionary = {
            'type': 'point',
            'center': self.center
        }
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        self.center = d['center']

    def xylim(self):
        xlim = [-1 + self.center[0], 1 + self.center[0]]
        ylim = [-1 + self.center[1], 1 + self.center[1]]
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
    point = Point(center=[-2, -2])
    point.show()
