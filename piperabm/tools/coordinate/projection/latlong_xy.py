from piperabm.tools.coordinate.projection.mercator import Mercator
from piperabm.tools.coordinate.projection.latlong_to_xyz import latlong_to_xyz, xyz_to_latlong
from piperabm.tools.linear_algebra import rotate
from piperabm.config.constants import EARTH_RADIUS


def latlong_to_xy(latitude_0, longitude_0, latitude, longitude):
    vector = latlong_to_xyz(latitude, longitude)
    vector = rotate.z(vector, longitude_0)
    vector = rotate.y(vector, -latitude_0)
    new_latitude, new_longitude = xyz_to_latlong(vector)
    x, y = Mercator.project(new_latitude, new_longitude, radius=EARTH_RADIUS)
    return x, y

def xy_to_latlong(latitude_0, longitude_0, x, y):
    new_latitude, new_longitude = Mercator.inverse(x, y, radius=EARTH_RADIUS)
    vector = latlong_to_xyz(new_latitude, new_longitude)
    vector = rotate.y(vector, latitude_0)
    vector = rotate.z(vector, -longitude_0)
    latitude, longitude = xyz_to_latlong(vector)
    return latitude, longitude


if __name__ == "__main__":
    latitude_0 = 70
    longitude_0 = -150

    latitude = latitude_0 + 1
    longitude = longitude_0 + 1

    x, y = latlong_to_xy(latitude_0, longitude_0, latitude, longitude)
    print(f"x, y: {x}, {y}")
    
    latitude, longitude = xy_to_latlong(latitude_0, longitude_0, x, y)
    print(f"latitude, longitude: {latitude}, {longitude}")