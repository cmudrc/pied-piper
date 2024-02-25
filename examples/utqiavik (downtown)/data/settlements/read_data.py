from piperabm.tools.coordinate.projection import latlong_xy

try:
    from coordinates import coordinates
    from meshes import meshes
except:
    from .coordinates import coordinates
    from .meshes import meshes


def read_data(latitude_0, longitude_0, permitted_labels='all'):
    """
    Read data from files and convert latitude/longitude to x,y only for permitted labels
    """
    result = []

    for id in meshes:
        if permitted_labels == 'all' or \
        id in permitted_labels:
            mesh = meshes[id]
            triangle = []
            for point in mesh:
                latlong = coordinates[point]
                latitude = latlong[0]
                longitude = latlong[1]
                x, y = latlong_xy(
                    latitude_0,
                    longitude_0,
                    latitude,
                    longitude
                )
                triangle.append([x, y])
            result.append(triangle)
    return result


if __name__ == "__main__":
    from labels import map_1 as permitted_labels

    latitude_0 = 0
    longitude_0 = 0

    data = read_data(latitude_0, longitude_0, permitted_labels)
    print(data[:5])
