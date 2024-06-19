import numpy as np

from piperabm.tools.vector import vector as vc


def latlong_xyz(latitude_degree=0, longitude_degree=0, radius=1):
    """
    Convert geographic coordinates (latitude, longitude) to 3D Cartesian coordinates (x, y, z).

    :param latitude_degree: The latitude of the point in degrees.
    :param longitude_degree: The longitude of the point in degrees.
    :return: A numpy array representing a vector (x, y, z).
    """
    # Convert angles to radians
    latitude_rad = np.radians(latitude_degree)
    longitude_rad = np.radians(longitude_degree)

    # Spherical to Cartesian conversion
    x = radius * np.cos(latitude_rad) * np.cos(longitude_rad)
    y = radius * np.cos(latitude_rad) * np.sin(longitude_rad)
    z = radius * np.sin(latitude_rad)

    return np.array([x, y, z])


def xyz_latlong(vector):
    """
    Convert 3D Cartesian coordinates (x, y, z) to geographic coordinates (latitude, longitude).

    :param vector: A numpy array representing a vector (x, y, z).
    :return: A tuple (latitude, longitude) in degrees.
    """
    if isinstance(vector, list):
        vector = np.array(vector)

    # Normalize the vector to ensure it has a magnitude of 1
    x, y, z = vc.normalize(vector)

    # Calculate latitude and longitude
    latitude_degree = np.degrees(np.arcsin(z))
    longitude_degree = np.degrees(np.arctan2(y, x))

    return latitude_degree, longitude_degree


if __name__ == '__main__':
    latitude = 70
    longitude = -150
    vector = latlong_xyz(latitude, longitude)
    print(vector)
    latitude, longitude = xyz_latlong(vector)
    print(latitude, longitude)
    
