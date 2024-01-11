from piperabm.tools.coordinate.projection import latlong_to_xy


def read(streets, labels, latitude_0, longitude_0):

    def create_segments(ls):
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
                # Convert point 1
                latlong_1 = labels[segment[0]]
                latitude_1 = latlong_1[0]
                longitude_1 = latlong_1[1]
                x_1, y_1 = latlong_to_xy(
                    latitude_0,
                    longitude_0,
                    latitude_1,
                    longitude_1
                )
                # Convert point 2
                latlong_2 = labels[segment[1]]
                latitude_2 = latlong_2[0]
                longitude_2 = latlong_2[1]
                x_2, y_2 = latlong_to_xy(
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