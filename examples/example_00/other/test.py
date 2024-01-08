from copy import deepcopy

from piperabm.model.samples import model_0 as model


first_entry = {}
print("1: ", model.create_delta(first_entry))


previous_entry = model.serialize()
print("2: ", previous_entry)

nodes = model.all_environment_nodes
node = nodes[0]
settlement = model.get(node)
settlement.degradation.add(10)

delta = model.create_delta(previous_entry)
print("3: ", delta)