from piperabm.tools.coordinate.projection import latlong_xy

from piperabm.data.utqiavik.streets.data import coordinates, streets


def read_streets(latitude_0, longitude_0, permitted_labels='all'):
    """
    Read data from files and convert latitude/longitude to x,y only for permitted labels
    """

    def create_segments(ls):
        """
        Split path to segments
        """
        result = []
        for i in range(1, len(ls)):
            entry = []
            entry.append(ls[i-1])
            entry.append(ls[i])
            result.append(entry)
        return result
    
    result = []
    for street in streets:
        name = street['name']
        paths = street['paths']
        for path in paths:
            segments = create_segments(path)
            for segment in segments:
                # Check permitted labels
                if permitted_labels == 'all' or \
                    (
                        segment[0] in permitted_labels and \
                        segment[1] in permitted_labels
                    ):
                    # Convert point 1
                    latlong_1 = coordinates[segment[0]]
                    latitude_1 = latlong_1[0]
                    longitude_1 = latlong_1[1]
                    x_1, y_1 = latlong_xy(
                        latitude_0,
                        longitude_0,
                        latitude_1,
                        longitude_1
                    )
                    # Convert point 2
                    latlong_2 = coordinates[segment[1]]
                    latitude_2 = latlong_2[0]
                    longitude_2 = latlong_2[1]
                    x_2, y_2 = latlong_xy(
                        latitude_0,
                        longitude_0,
                        latitude_2,
                        longitude_2
                    )
                    # Create entry
                    entry = {
                        'name': name,
                        'pos_1': [x_1, y_1],
                        'pos_2': [x_2, y_2]
                    }
                    result.append(entry)
    return result


if __name__ == '__main__':
    from labels import map_1 as permitted_labels

    latitude_0 = 0
    longitude_0 = 0

    data = read_streets(latitude_0, longitude_0, permitted_labels)
    print(data[:5])
