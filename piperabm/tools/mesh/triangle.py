import random


class Triangle:
    """
    Represent a single triangle for meshing purpose.

    Parameters
    ----------
    point_1 : list
        `x` and `y` coordinates of the vertice 1.
    point_2 : list
        `x` and `y` coordinates of the vertice 1.
    point_3 : list
        `x` and `y` coordinates of the vertice 1.
    density : float, default=1
        The higher the density is, the higher the chance of containing the point is.
    """

    def __init__(self, point_1: list, point_2: list, point_3: list, density: float = 1):
        self.A = point_1
        self.B = point_2
        self.C = point_3
        self.density = density

    @property
    def area(self):
        """
        Calculate the area of the triangle.
        """
        x1, y1 = self.A
        x2, y2 = self.B
        x3, y3 = self.C
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0

    def random_point(self) -> list:
        """
        Generate a random point inside the triangle using Barycentric coordinates.
        """
        r1, r2 = random.random(), random.random()
        sqrt_r1 = r1**0.5
        a = 1 - sqrt_r1
        b = sqrt_r1 * (1 - r2)
        c = r2 * sqrt_r1
        # Calculate the random point's coordinates
        x = a * self.A[0] + b * self.B[0] + c * self.C[0]
        y = a * self.A[1] + b * self.B[1] + c * self.C[1]
        return [x, y]

    @property
    def weight(self) -> float:
        """
        Both area and density are proportional to the probability of containing a point inside. Therefore, weight is defined as a more suitable parameter for point generation.
        """
        return self.area * self.density


if __name__ == "__main__":
    pos_1 = [0, 0]
    pos_2 = [2, 0]
    pos_3 = [0, 1]
    triangle = Triangle(pos_1, pos_2, pos_3)
    print(triangle.area)
