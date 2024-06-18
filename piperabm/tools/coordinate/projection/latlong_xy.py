from piperabm.tools.coordinate.projection.mercator import Mercator
from piperabm.tools.coordinate.projection.latlong_xyz import latlong_xyz, xyz_latlong
from piperabm.tools.coordinate import rotate


EARTH_RADIUS = 6378000 # meters


def latlong_xy(latitude_0=0, longitude_0=0, latitude=0, longitude=0):
    """
    Convert (latitude, logitude) to (x, y).

    :param latitude_0: latitude of the point which will be projected to (x=0, y=0).
    :param longitude_0: longitude of the point which will be projected to (x=0, y=0).
    :return: (x, y)
    """
    vector = latlong_xyz(latitude, longitude)
    vector = rotate.z(vector, longitude_0)
    vector = rotate.y(vector, -latitude_0)
    new_latitude, new_longitude = xyz_latlong(vector)
    x, y = Mercator.project(new_latitude, new_longitude, radius=EARTH_RADIUS)
    return x, y

def xy_latlong(latitude_0=0, longitude_0=0, x=0, y=0):
    """
    Convert (x, y) to (latitude, logitude).

    :param latitude_0: latitude of the point which will be projected to (x=0, y=0).
    :param longitude_0: longitude of the point which will be projected to (x=0, y=0).
    :return: (latitude, logitude)
    """
    new_latitude, new_longitude = Mercator.inverse(x, y, radius=EARTH_RADIUS)
    vector = latlong_xyz(new_latitude, new_longitude)
    vector = rotate.y(vector, latitude_0)
    vector = rotate.z(vector, -longitude_0)
    latitude, longitude = xyz_latlong(vector)
    return latitude, longitude


if __name__ == '__main__':
    latitude_0 = 70
    longitude_0 = -150

    latitude = latitude_0 + 1
    longitude = longitude_0 + 1

    x, y = latlong_xy(latitude_0, longitude_0, latitude, longitude)
    print(f'x, y: {x}, {y}')
    
    latitude, longitude = xy_latlong(latitude_0, longitude_0, x, y)
    print(f'latitude, longitude: {latitude}, {longitude}')