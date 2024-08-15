import os

import piperabm as pa
from piperabm.society.samples.society_2 import model


# Setup
path = os.path.dirname(os.path.realpath(__file__))
model.path = path
model.society.max_time_outside = 700
model.society.activity_cycle = 2000
model.society.average_income = 10
model.infrastructure.coeff_usage = 0
model.infrastructure.coeff_weather = 0

# Run
print(">>> Running...")
model.run(n=1000, save=True, resume=False, report=True, step_size=10)

# Measure
print(">>> Measuring...")
measurement = pa.Measurement(path=path)
measurement.measure(resume=False, report=True)