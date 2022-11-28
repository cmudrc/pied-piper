import numpy as np

from piperabm.graphics.plt.boundery import boundery_to_plt


class Boundery:
    """
    Define an enclosed area in space.
    """

    def __init__(self):
        self.center = None # position of center of boundery in [x, y] form

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

    def to_plt(self, ax=None, active=True):
        """
        Add the required elements to plt
        """
        boundery_to_plt(self.to_dict(), ax, active)


if __name__ == "__main__":
    pass
