from piperabm.tools.coordinate.projection.mercator import Mercator
from piperabm.tools.coordinate.projection.latlong_xyz import latlong_xyz, xyz_latlong
from piperabm.tools.coordinate import rotate


"""
Coordinate projection utilities converting between geographic (latitude, longitude) and Cartesian (x, y) coordinates.

This module uses 3D rotation and Mercator projection to:
- Convert latitude/longitude to local x/y (latlong_xy).
- Convert local x/y back to latitude/longitude (xy_latlong).

"""

EARTH_RADIUS = 6378000  # meters


def latlong_xy(
    latitude_0: float = 0.0,
    longitude_0: float = 0.0,
    latitude: float = 0.0,
    longitude: float = 0.0,
) -> tuple[float, float]:
    """
    Convert geographic coordinates to Cartesian (x, y) using a Mercator projection around a specified origin.

    :param float latitude_0: Latitude of the projection origin, in degrees.
    :param float longitude_0: Longitude of the projection origin, in degrees.
    :param float latitude: Latitude of the point to project, in degrees.
    :param float longitude: Longitude of the point to project, in degrees.
    :return: A tuple `(x, y)` of projected coordinates in meters.
    :rtype: tuple(float, float)
    """
    vector = latlong_xyz(latitude, longitude)
    vector = rotate.z(vector, longitude_0)
    vector = rotate.y(vector, -latitude_0)
    new_latitude, new_longitude = xyz_latlong(vector)
    x, y = Mercator.project(new_latitude, new_longitude, radius=EARTH_RADIUS)
    return x, y


def xy_latlong(
    latitude_0: float = 0.0, longitude_0: float = 0.0, x: float = 0.0, y: float = 0.0
) -> tuple[float, float]:
    """
    Convert Cartesian (x, y) back to geographic coordinates around a specified origin using the inverse Mercator projection.

    :param float latitude_0: Latitude of the projection origin, in degrees.
    :param float longitude_0: Longitude of the projection origin, in degrees.
    :param float x: X coordinate in meters relative to the projection origin.
    :param float y: Y coordinate in meters relative to the projection origin.
    :return: A tuple `(latitude, longitude)` of geographic coordinates in degrees.
    :rtype: tuple(float, float)
    """
    new_latitude, new_longitude = Mercator.inverse(x, y, radius=EARTH_RADIUS)
    vector = latlong_xyz(new_latitude, new_longitude)
    vector = rotate.y(vector, latitude_0)
    vector = rotate.z(vector, -longitude_0)
    latitude, longitude = xyz_latlong(vector)
    return latitude, longitude


def _example():  # pragma: no cover
    latitude_0 = 70
    longitude_0 = -150

    latitude = latitude_0 + 1
    longitude = longitude_0 + 1

    x, y = latlong_xy(latitude_0, longitude_0, latitude, longitude)
    print(f"x, y: {x}, {y}")

    latitude, longitude = xy_latlong(latitude_0, longitude_0, x, y)
    print(f"latitude, longitude: {latitude}, {longitude}")


if __name__ == "__main__":
    _example()
