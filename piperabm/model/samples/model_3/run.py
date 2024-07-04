import os

import piperabm as pa
from piperabm.infrastructure.samples import model_2 as model


path = os.path.dirname(os.path.realpath(__file__))
name = 'model'

# Setup
model.path = path
model.name = name
model.society.neighbor_radius = 270
model.society.generate_agents(
    num=10,
    gini_index=0.45,
    average_balance=100
)

# Run
model.run(n=50, save=True, resume=False, report=True, step_size=10)

# Measure
measurement = pa.Measurement(path, name=name)
measurement.measure(resume=False, report=True)