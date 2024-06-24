import os

from piperabm.measurement import Measurement
from piperabm.time import Date


start = Date.today()
path = os.path.dirname(os.path.realpath(__file__))
measurement = Measurement(path, name='model')
measurement.measure(resume=False, report=True)
end = Date.today()
print(end - start)