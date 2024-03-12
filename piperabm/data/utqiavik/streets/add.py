from piperabm.infrastructure import Road
from piperabm.data.utqiavik.streets.read_streets import read_streets
from piperabm.data.utqiavik.info import location


def add_streets_to_model(model, streets_permitted_labels='all'):
    streets_data = read_streets(
        latitude_0=location['latitude'],
        longitude_0=location['longitude'],
        permitted_labels=streets_permitted_labels
    )
    for street_data in streets_data:
        road = Road(
            pos_1=street_data['pos_1'],
            pos_2=street_data['pos_2'],
            name=street_data['name']
        )
        model.add(road)
    return model
