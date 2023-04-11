from piperabm.boundary.circular import Circular


class Point(Circular):
    """
    Create a infitesimal circular boundery in space
    """

    def __init__(self):
        super().__init__(
            radius=1
        )
        self.type = 'point'

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


if __name__ == "__main__":
    boundary = Point()
    boundary.center = [-2, -2]
    print(boundary)