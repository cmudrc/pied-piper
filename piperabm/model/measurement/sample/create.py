import os

from piperabm.model.measurement import Measurement


path = os.path.dirname(os.path.realpath(__file__))

measure = Measurement(path=path, name='model')
hour = 3600
measure.add_time(0 * hour) # Base

# 1
measure.add_time(value=1*hour)
measure.add_accessibility(id=1, value={'food': 1, 'water': 1, 'energy': 1})
measure.add_accessibility(id=2, value={'food': 0.8, 'water': 0.7, 'energy': 0.6})
measure.add_travel_distance(value=1.1)
# 2
measure.add_time(value=2*hour)
measure.add_accessibility(id=1, value={'food': 0.9, 'water': 0.8, 'energy': 0.7})
measure.add_accessibility(id=2, value={'food': 0.5, 'water': 0.6, 'energy': 0.4})
measure.add_travel_distance(value=0.9)
# 3
measure.add_time(value=3*hour)
measure.add_accessibility(id=1, value={'food': 0.8, 'water': 0.7, 'energy': 0.6})
measure.add_accessibility(id=2, value={'food': 0.2, 'water': 0.4, 'energy': 0.3})
measure.add_travel_distance(value=0.3)
# 4
measure.add_time(value=4*hour)
measure.add_accessibility(id=1, value={'food': 0.7, 'water': 0.6, 'energy': 0.5})
measure.add_accessibility(id=2, value={'food': 0, 'water': 0.3, 'energy': 0.2})
measure.add_travel_distance(value=0.46)
# 5
measure.add_time(value=5*hour)
measure.add_accessibility(id=1, value={'food': 0.6, 'water': 0.5, 'energy': 0.4})
measure.add_accessibility(id=2, value={'food': 0, 'water': 0.3, 'energy': 0.2})
measure.add_travel_distance(value=0.2)

measure.save()