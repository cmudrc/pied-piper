from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement

from data.streets.read_data import read_streets
from data.settlements.generate_settlements import generate_settlements
from data.info import *


def create_model(
        streets_permitted_labels='all',
        settlements_permitted_labels='all'
    ):
    """
    Construct model using data from files
    """
    model = Model(
        name=name,
        proximity_radius=proximity_radius,
        gini_index=gini_index
    )
    
    latitude_0 = location['latitude']
    longitude_0 = location['longitude']

    streets_data = read_streets(latitude_0, longitude_0, permitted_labels=streets_permitted_labels)
    for street_data in streets_data:
        road = Road(
            pos_1=street_data['pos_1'],
            pos_2=street_data['pos_2'],
            name=street_data['name']
        )
        model.add(road)

    settlements_data = generate_settlements(settlements_num, latitude_0, longitude_0, permitted_labels=settlements_permitted_labels)
    for settlement_data in settlements_data:
        settlement = Settlement(pos=settlement_data)
        model.add(settlement)

    return model


if __name__ == '__main__':
    import os

    from data.streets.labels import filter_labels as filter_street_labels
    from data.settlements.labels import filter_labels as filter_settlement_labels

    point_1_latitude, point_1_longitude = 71.322109, -156.688674
    point_2_latitude, point_2_longitude = 71.333940, -156.665691
    latitude_min = min([point_1_latitude, point_2_latitude])
    latitude_max = max([point_1_latitude, point_2_latitude])
    longitude_min = min([point_1_longitude, point_2_longitude])
    longitude_max = max([point_1_longitude, point_2_longitude])

    streets_permitted_labels = filter_street_labels(
        latitude_min,
        latitude_max,
        longitude_min,
        longitude_max
    )
    settlements_permitted_labels = filter_settlement_labels(
        latitude_min,
        latitude_max,
        longitude_min,
        longitude_max
    )
    
    model = create_model(streets_permitted_labels, settlements_permitted_labels)
    model.path = os.path.dirname(os.path.realpath(__file__))
    model.save_initial()
