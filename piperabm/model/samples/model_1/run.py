import os

import piperabm as pa
from piperabm.society.samples.society_1 import model


# Setup
path = os.path.dirname(os.path.realpath(__file__))
model.path = path

# Run
print(">>> Running...")
model.run(n=500, save=True, resume=False, report=True, step_size=100)

# Measure
print(">>> Measuring...")
measurement = pa.Measurement(path=path)
measurement.measure(resume=False, report=True)
