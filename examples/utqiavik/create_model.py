from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement

from data.streets.read_data import read_streets
from data.settlements.generate_settlements import generate_settlements
from data.info import *


def create_model(streets_permitted_labels='all', settlements_permitted_labels='all'):
    """
    Construct model using data from files
    """
    model = Model(
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

    settlements_data = generate_settlements(300, latitude_0, longitude_0, permitted_labels=settlements_permitted_labels)
    #settlements_data = generate_settlements(settlements_num, latitude_0, longitude_0, permitted_labels=settlements_permitted_labels)
    for settlement_data in settlements_data:
        settlement = Settlement(pos=settlement_data)
        model.add(settlement)

    return model


if __name__ == '__main__':
    from data.streets.labels import map_1 as streets_permitted_labels
    from data.settlements.labels import map_1 as settlements_permitted_labels


    model = create_model(
        streets_permitted_labels=streets_permitted_labels,
        settlements_permitted_labels=settlements_permitted_labels   
    )

    #model = create_model()
    model.show()
