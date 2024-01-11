from piperabm.model import Model
from piperabm.infrastructure import Road

from read import read


def load(streets, labels):
    latitude_0 = 71.30
    longitude_0 = -156.75

    data = read(streets, labels, latitude_0, longitude_0)

    model = Model(proximity_radius=10)

    for entry in data:
        road = Road(
            pos_1=entry['pos_1'],
            pos_2=entry['pos_2'],
            name=entry['name']
        )
        model.add(road)
    return model
