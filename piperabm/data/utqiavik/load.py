from piperabm.data.utqiavik.info import location
from piperabm.data.utqiavik.streets.load import load_street_objects, filter_street_objects
from piperabm.data.utqiavik.homes.load import load_home_objects, filter_home_objects
from piperabm.data.utqiavik.markets.load import load_market_objects, filter_market_objects


def add_to_model(
        model,
        streets: bool = True,
        homes: bool = True,
        markets: bool = True,
        homes_count: bool = None,
        latitude_min: float = None,
        latitude_max: float = None,
        longitude_min: float = None,
        longitude_max: float = None,
        x_min: float = None,
        x_max: float = None,
        y_min: float = None,
        y_max: float = None
    ):

    latitude_0 = location['latitude']
    longitude_0 = location['longitude']

    if streets is True:
        street_objects = load_street_objects(
            latitude_0=latitude_0,
            longitude_0=longitude_0,
            latitude_min=latitude_min,
            latitude_max=latitude_max,
            longitude_min=longitude_min,
            longitude_max=longitude_max,
        )
        street_objects = filter_street_objects(
            streets=street_objects,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max
        )
        for object in street_objects:
            model.add(object)

    if homes is True:
        home_objects = load_home_objects(
            latitude_0=latitude_0,
            longitude_0=longitude_0,
            latitude_min=latitude_min,
            latitude_max=latitude_max,
            longitude_min=longitude_min,
            longitude_max=longitude_max,
        )
        home_objects = filter_home_objects(
            homes=home_objects,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max
        )
        if homes_count is not None:
            if homes_count <= len(home_objects):
                home_objects = home_objects[:homes_count]
        for object in home_objects:
            model.add(object)

    if markets is True:
        market_objects = load_market_objects(
            latitude_0=latitude_0,
            longitude_0=longitude_0,
            latitude_min=latitude_min,
            latitude_max=latitude_max,
            longitude_min=longitude_min,
            longitude_max=longitude_max,
        )
        market_objects = filter_market_objects(
            markets=market_objects,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max
        )
        for object in market_objects:
            model.add(object)

    return model


if __name__ == "__main__":

    from piperabm.infrastructure_new import Infrastructure
    
    infrastructure = Infrastructure()
    infrastructure = add_to_model(
        model=infrastructure,
        streets=True,
        homes=True,
        markets=True,
        latitude_min=None,
        latitude_max=None,
        longitude_min=None,
        longitude_max=None,
        x_min=-1000,
        x_max=1500,
        y_min=-600,
        y_max=1000
    )
    #infrastructure.bake(report=True)
    print(infrastructure.stat)
    infrastructure.show()