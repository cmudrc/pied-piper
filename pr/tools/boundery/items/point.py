import matplotlib.pyplot as plt

from pr.tools.boundery.items import Circular


class Point(Circular):
    """
    Create a infitesimal circular boundery in space
    """
    
    def __init__(self, center):
        super().__init__(
            center=center,
            radius=0
        )

    def to_dict(self):
        dictionary = {
            'type': 'point',
            'center': self.center
        }
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        self.center = d['center']


if __name__ == "__main__":
    point = Point(center=[-2, -2])
    point.show()