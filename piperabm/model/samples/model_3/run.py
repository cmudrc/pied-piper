import os
from copy import deepcopy

import piperabm as pa
from piperabm.infrastructure.samples.infrastructure_3 import model as model_3


path = os.path.dirname(os.path.realpath(__file__))

# Setup
model = deepcopy(model_3)
model.path = path
model.society.neighbor_radius = 270
model.society.generate(
    num=10,
    gini_index=0.45,
    average_balance=100
)

# Run
model.run(n=50, save=True, resume=False, report=True, step_size=10)

# Measure
measurement = pa.Measurement(path)
measurement.measure(resume=False, report=True)