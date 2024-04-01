from piperabm.tools.coordinate.projection import latlong_xy
from piperabm.data.utqiavik.markets.data.coordinates import coordinates
from piperabm.infrastructure_new import Market


def read_markets_data(
        latitude_0: float = 0,
        longitude_0: float = 0,
        permitted_labels = "all"
    ):
    """
    Read data from files and convert latitude/longitude to x,y only for permitted labels
    """
    result = []
    for label in coordinates:
        name = coordinates[label]["name"]
        location = coordinates[label]["location"]
        # Check permitted labels
        if permitted_labels == "all" or \
        label in permitted_labels:
            x, y = latlong_xy(
                latitude_0,
                longitude_0,
                latitude=location[0],
                longitude=location[1]
            )
            position = [x, y]
            result.append([name, position])
    return result

def filter_market_labels(
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
            coordinate = coordinates[id]['location']
            latitude = coordinate[0]
            longitude = coordinate[1]
            if latitude >= latitude_min and \
            latitude <= latitude_max and \
            longitude >= longitude_min and \
            longitude <= longitude_max:
                permitted_labels.append(id)
    return permitted_labels

def load_market_objects(
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
    permitted_labels = filter_market_labels(
        latitude_min,
        latitude_max,
        longitude_min,
        longitude_max
    )
    markets_data = read_markets_data(latitude_0, longitude_0, permitted_labels)
    markets = []
    for market_data in markets_data:
        market = Market(
            pos=market_data[1],
            name=market_data[0]
        )
        markets.append(market)
    return markets

def filter_market_objects(
        markets: list,
        x_min: float = None,
        x_max: float = None,
        y_min: float = None,
        y_max: float = None
    ):
    if x_min is None or \
    x_max is None or \
    y_min is None or \
    y_max is None:
        result = markets
    else:
        result = []
        for market in markets:
            pos = market.pos
            pos_x = pos[0]
            pos_y = pos[1]
            if pos_x <= x_max and \
            pos_x >= x_min and \
            pos_y <= y_max and \
            pos_y >= y_min:
                result.append(market)
    return result