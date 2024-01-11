from piperabm.model import Model
from piperabm.infrastructure import Road

from data.read_data import read_data


def create_model(streets, labels):
    latitude_0 = 71.30
    longitude_0 = -156.75

    data = read_data(streets, labels, latitude_0, longitude_0)

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

    from data.labels import labels
    from data.streets import streets

    model = create_model(streets, labels)
    model.show()
