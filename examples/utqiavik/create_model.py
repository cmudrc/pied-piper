from piperabm.model import Model
from piperabm.infrastructure import Road

from data.read_data import read_data


def create_model(streets, labels, permitted_labels='all'):
    latitude_0 = 71.30
    longitude_0 = -156.75

    data = read_data(streets, labels, latitude_0, longitude_0, permitted_labels)

    model = Model(proximity_radius=10)

    for entry in data:
        road = Road(
            pos_1=entry['pos_1'],
            pos_2=entry['pos_2'],
            name=entry['name']
        )
        model.add(road)
    return model


if __name__ == '__main__':

    from examples.utqiavik.data.coordinates import coordinates
    from data.streets import streets
    from data.labels import map_4 as permitted_labels

    model = create_model(streets, coordinates, permitted_labels)
    model.show()
