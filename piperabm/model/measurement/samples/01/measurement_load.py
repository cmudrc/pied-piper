import os

from piperabm.measurement import Measurement


path = os.path.dirname(os.path.realpath(__file__))
measurement = Measurement(path, name='model')
measurement.load()


if __name__ == "__main__":

    _from = 6
    _to = None

    dates = measurement.date(
        _from=_from,
        _to=_to
    )
    accessibilities = measurement.accessibility(
        agents='all',
        resources='all',
        _from=_from,
        _to=_to
    )
    travel_distances = measurement.travel_distance(
        _from=_from,
        _to=_to
    )
    print(dates)
    print(accessibilities)
    print(travel_distances)