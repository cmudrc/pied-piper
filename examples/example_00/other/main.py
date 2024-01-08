import os

from piperabm.model.samples import model_0 as model
from piperabm.tools.file_manager import JsonHandler as jsh


def save(model, path):
    filename = model.name
    if not jsh.exists(path, filename):
        data = [{}]
        jsh.save(data, path, filename)
    data = jsh.load(path, filename)
    previous_entry = data[-1]
    #print(previous_entry)
    delta = model.create_delta(previous_entry)
    jsh.append(delta, path, filename)


path = os.path.dirname(os.path.realpath(__file__))

save(model, path)

data = jsh.load(path, model.name)
delta = model.create_delta(data[-1])
print(delta)

nodes = model.all_environment_nodes
node = nodes[0]
settlement = model.get(node)
settlement.degradation.add(10)



#save(model, path)

#data = jsh.load(path, model.name)
#print(data)
#print(data[-1])
