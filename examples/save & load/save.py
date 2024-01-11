'''
This example creates a save file for a sample model
'''

import os

from piperabm.model.samples import model_2 as model


path = os.path.dirname(os.path.realpath(__file__))

model.remove_save(path)  # clean previous save

model.save(path)

# Some changes happen to the model
edges = model.all_environment_edges
index = edges[0]
road = model.get(index)
road.degradation.add(10)

model.save(path)
