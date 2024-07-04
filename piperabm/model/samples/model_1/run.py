import os

import piperabm as pa
from piperabm.infrastructure.samples import model_1 as model


path = os.path.dirname(os.path.realpath(__file__))
name = 'model'

# Setup
model.path = path
model.name = name
id_agent = 0
model.society.add_agent(
    id=id_agent,
    food=1,
    water=1,
    energy=1,
    balance=100
)

# Run
model.run(n=500, save=True, resume=False, report=True, step_size=100)

# Measure
measurement = pa.Measurement(path, name=name)
measurement.measure(resume=False, report=True)