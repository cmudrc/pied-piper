'''
This example creates a save file for a sample model
'''

import os

from piperabm.model.samples import model_0 as model


path = os.path.dirname(os.path.realpath(__file__))
filename = model.name

model.remove_save(path)  # clean previous save

model.save(path)

nodes = model.all_environment_nodes
node = nodes[0]
settlement = model.get(node)
settlement.degradation.add(10)

model.save(path)
