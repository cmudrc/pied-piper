from piperabm.tools.coordinate.projection import latlong_xy
from piperabm.data.utqiavik.streets.data import coordinates, streets
from piperabm.infrastructure_new import Street


def read_streets_data(
        latitude_0: float = 0,
        longitude_0: float = 0,
        permitted_labels = "all"
    ):
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
        name = street["name"]
        paths = street["paths"]
        for path in paths:
            segments = create_segments(path)
            for segment in segments:
                # Check permitted labels
                if permitted_labels == "all" or \
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
                        "name": name,
                        "pos_1": [x_1, y_1],
                        "pos_2": [x_2, y_2]
                    }
                    result.append(entry)
    return result

def filter_street_labels(
        latitude_min: float = None,
        latitude_max: float = None,
        longitude_min: float = None,
        longitude_max: float = None
    ):
    """
    Filter data labels based on their latitude and longitude
    """
    if latitude_min is None or \
    latitude_max is None or \
    longitude_min is None or \
    longitude_max is None:
        permitted_labels = 'all'
    else:
        permitted_labels = []
        for id in coordinates:
            coordinate = coordinates[id]
            latitude = coordinate[0]
            longitude = coordinate[1]
            if latitude >= latitude_min and \
            latitude <= latitude_max and \
            longitude >= longitude_min and \
            longitude <= longitude_max:
                permitted_labels.append(id)
    return permitted_labels

def load_street_objects(
        latitude_0: float = 0,
        longitude_0: float = 0,
        latitude_min: float = None,
        latitude_max: float = None,
        longitude_min: float = None,
        longitude_max: float = None
    ):
    """
    Return a list of street objects
    """
    streets = []
    permitted_labels = filter_street_labels(
        latitude_min,
        latitude_max,
        longitude_min,
        longitude_max
    )
    streets_data = read_streets_data(latitude_0, longitude_0, permitted_labels)
    for street_data in streets_data:
        street = Street(
            pos_1=street_data['pos_1'],
            pos_2=street_data['pos_2'],
            name=street_data['name']
        )
        streets.append(street)
    return streets

def filter_street_objects(
        streets: list,
        x_min: float = None,
        x_max: float = None,
        y_min: float = None,
        y_max: float = None
    ):
    if x_min is None or \
    x_max is None or \
    y_min is None or \
    y_max is None:
        result = streets
    else:
        result = []
        for street in streets:
            pos_1 = street.pos_1
            pos_1_x = pos_1[0]
            pos_1_y = pos_1[1]
            pos_2 = street.pos_2
            pos_2_x = pos_2[0]
            pos_2_y = pos_2[1]
            if pos_1_x <= x_max and \
            pos_1_x >= x_min and \
            pos_2_x <= x_max and \
            pos_2_x >= x_min and \
            pos_1_y <= y_max and \
            pos_1_y >= y_min and \
            pos_2_y <= y_max and \
            pos_2_y >= y_min:
                result.append(street)
    return result


if __name__ == "__main__":

    from piperabm.data.utqiavik.streets.data.labels.labels import map_1 as permitted_labels

    latitude_0 = 0
    longitude_0 = 0

    data = read_streets_data(latitude_0, longitude_0, permitted_labels)
    print(data[:5])
