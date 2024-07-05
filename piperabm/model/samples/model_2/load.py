import os

import piperabm as pa


path = os.path.dirname(os.path.realpath(__file__))
measurement = pa.Measurement(path=path)
measurement.load()


if __name__ == "__main__":
    _from = None
    _to = None
    agents='all'
    resources='all'
    measurement.accessibility.show(agents, resources, _from, _to)
    measurement.travel_distance.show(_from, _to)
