import os

import piperabm as pa


path = os.path.dirname(os.path.realpath(__file__))
measurement = pa.Measurement(path, name='model')
measurement.load()


if __name__ == "__main__":

    _from = None
    _to = None
    agents='all'
    resources='food'

    measurement.accessibility.show(agents, resources, _from, _to)
    measurement.travel_distance.show(_from, _to)

    '''
    dates = measurement.filter_times(
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
    '''
