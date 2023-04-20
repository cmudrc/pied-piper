from random import uniform #######
import numpy as np

from piperabm.tools.symbols import SYMBOLS
from piperabm.boundary.shapes.shape import Shape
from piperabm.tools.coordinate import rotate_coordinate


class Rectangle(Shape):

    def __init__(
            self,
            width: float=None,
            height: float=None,
            angle: float=0
        ):
        if width is None:
            width = SYMBOLS['eps']
        if height is None:
            height = SYMBOLS['eps']
        super().__init__()
        self.width = width
        self.height = height
        self.angle = angle
        self.type = 'rectangle'

    def size(self):
        return self.width * self.height

    def point_distance_from_body(self, point: list=[0, 0]):
        """
        Calculate distance from body, negative when located inside
        """
        def diagonal_slope(pos_prime):
            x = pos_prime[0]
            y = pos_prime[1]
            if x != 0:
                slope = y / x
            else:
                slope = SYMBOLS['inf']
            return slope
        
        distance = None
        pos_prime = rotate_coordinate(point, self.angle)
        slope = diagonal_slope(pos_prime)
        slope_angle = np.arctan(slope)
        if slope <= self.height / self.width:
            center_to_boundery = (self.width / 2) / np.cos(slope_angle)
        else:
            center_to_boundery = (self.height / 2) / np.sin(slope_angle)
        distance = self.distance(point, mode='center') - center_to_boundery
        return distance

    def rand_pos(self) -> list:
        pos = [uniform(-self.width/2, self.width/2),
               uniform(-self.height/2, self.height/2)]
        new_pos = rotate_coordinate(pos, -self.angle)
        return new_pos

    def to_dict(self) -> dict:
        dictionary = super().to_dict()
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        dictionary['angle'] = self.angle
        return dictionary

    def from_dict(self, dictionary: dict) -> None:
        super().from_dict(dictionary)
        self.width = dictionary['width'] 
        self.height = dictionary['height']
        self.angle = dictionary['angle']


if __name__ == "__main__":
    shape = Rectangle(width=4, height=3, angle=0)
    print(shape)
