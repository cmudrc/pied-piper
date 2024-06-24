import os

from piperabm.model.measurement import Measurement


path = os.path.dirname(os.path.realpath(__file__))

measure = Measurement(path=path, name='model')
measure.load()

agents = 'all'
resources = 'all'
_from = None
_to = None
print("travel distances: ", measure.travel_distance(_from=_from, _to=_to))
print("accessibilities: ", measure.accessibility(agents=agents, resources=resources, _from=_from, _to=_to))
print("average: ", measure.accessibility.average(agents=agents, resources=resources))