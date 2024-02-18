from piperabm.tools.coordinate.projection import latlong_xy


def read_data(meshs, coordinates, latitude_0, longitude_0, permitted_labels='all'):
    """
    Read data from files and convert latitude/longitude to x,y only for permitted labels
    """
    result = []

    for id in meshs:
        if permitted_labels == 'all' or \
        id in permitted_labels:
            mesh = meshs[id]
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

    from coordinates import coordinates
    from meshs import meshs
    from labels import map_1 as permitted_labels

    latitude_0 = 0
    longitude_0 = 0

    data = read_data(meshs, coordinates, latitude_0, longitude_0, permitted_labels)
    print(data[:5])
