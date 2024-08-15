import os

import piperabm as pa
from piperabm.society.samples.society_1 import model


# Setup
path = os.path.dirname(os.path.realpath(__file__))
model.path = path
model.society.max_time_outside = 300
model.society.activity_cycle = 1000
model.society.average_income = 10
model.infrastructure.coeff_usage = 0.3

# Run
print(">>> Running...")
model.run(n=1000, save=True, resume=False, report=True, step_size=10)

# Measure
print(">>> Measuring...")
measurement = pa.Measurement(path=path)
measurement.measure(resume=False, report=True)