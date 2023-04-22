from piperabm.object import Object
from piperabm.tools.coordinate import euclidean_distance


class Shape(Object):
    
    def __init__(self):
        super().__init__()
        self.type = 'shape'

    def is_in(self, point: list=[0, 0]):
        """
        Check whether *point* is located within the shape
        """
        result = False
        distance = self.distance(point, mode='body')
        if distance <= 0:
            result = True
        return result

    def point_distance_from_center(self, point: list=[0, 0]) -> float:
        """
        Calculate the distance from center
        """
        center = [0, 0]
        return euclidean_distance(center, point)

    def point_distance_from_body(self, point: list=[0, 0]) -> float:
        """
        Calculate distance from body, negative when located inside
        """
        print("NOT IMPLEMENTED YET")
        return None
    
    def size(self):
        print("NOT IMPLEMENTED YET")
        return None

    def point_distance(self, point: list=[0, 0], mode='center') -> float:
        """
        Calculate the distance from a point [x, y]
        """
        result = None
        if mode == 'center':
            result = self.point_distance_from_center(point)
        elif mode == 'body':
            result = self.point_distance_from_body(point)
        return result

    def distance(self, other, mode='center') -> float:
        """
        Calculate the distance
        """
        result = None
        if isinstance(other, list): # point
            result = self.point_distance(point=other, mode=mode)
        return result

    def to_dict(self) -> dict:
        return {
            'type': self.type,
        }

    def from_dict(self, dictionary: dict):
        self.type = dictionary['type']


if __name__ == "__main__":
    shape = Shape()
    print(shape)