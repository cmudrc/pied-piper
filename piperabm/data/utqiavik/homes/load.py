from piperabm.tools.coordinate.projection import latlong_xy
from piperabm.data.utqiavik.homes.generated_data.load import load
from piperabm.infrastructure_new import Home


def filter_homes_data(
        homes_data,
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
        result = homes_data
    else:
        result = []
        for location in homes_data:
            latitude = location[0]
            longitude = location[1]
            if latitude >= latitude_min and \
            latitude <= latitude_max and \
            longitude >= longitude_min and \
            longitude <= longitude_max:
                result.append(location)
    return result

def load_home_objects(
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
    homes = []
    homes_data = load()
    homes_data = filter_homes_data(
        homes_data,
        latitude_min,
        latitude_max,
        longitude_min,
        longitude_max
    )
    for home_data in homes_data:
        x, y = latlong_xy(
            latitude_0,
            longitude_0,
            latitude=home_data[0],
            longitude=home_data[1]
        )
        point = [x, y]
        home = Home(pos=point)
        homes.append(home)
    return homes

def filter_home_objects(
        homes: list,
        x_min: float = None,
        x_max: float = None,
        y_min: float = None,
        y_max: float = None
    ):
    if x_min is None or \
    x_max is None or \
    y_min is None or \
    y_max is None:
        result = homes
    else:
        result = []
        for home in homes:
            pos = home.pos
            pos_x = pos[0]
            pos_y = pos[1]
            if pos_x <= x_max and \
            pos_x >= x_min and \
            pos_y <= y_max and \
            pos_y >= y_min:
                result.append(home)
    return result