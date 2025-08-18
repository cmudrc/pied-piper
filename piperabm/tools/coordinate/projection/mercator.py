import numpy as np


class Mercator:

    @staticmethod
    def project(
        latitude_degree: float = 0.0, longitude_degree: float = 0.0, radius: float = 1.0
    ):
        """
        Project using Mercator formula to cartesian coordinates.
        """
        latitude_rad = np.radians(latitude_degree)
        longitude_rad = np.radians(longitude_degree)
        x = radius * longitude_rad
        y = radius * np.log(np.tan(np.pi / 4 + latitude_rad / 2))
        return x, y

    @staticmethod
    def inverse(x: float = 0.0, y: float = 0.0, radius: float = 1.0):
        """
        Inverse project from Cartesian coordinates to (latitude, longitude) in degrees.
        """
        longitude_rad = x / radius
        latitude_rad = 2 * np.arctan(np.exp(y / radius)) - np.pi / 2
        latitude_degree = np.degrees(latitude_rad)
        longitude_degree = np.degrees(longitude_rad)
        return latitude_degree, longitude_degree


if __name__ == "__main__":
    latitude = 70
    longitude = -150
    radius = 6378
    x, y = Mercator.project(latitude, longitude, radius)
    print(x, y)
    latitude, longitude = Mercator.inverse(x, y, radius)
    print(latitude, longitude)
