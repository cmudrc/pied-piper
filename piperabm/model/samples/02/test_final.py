import os

import piperabm as pa


path = os.path.dirname(os.path.realpath(__file__))
model = pa.Model(path=path, name='model')
model.load_final()
print(model.society.get_resource('energy', 0))
print(model.society.get_enough_resource('energy', 0))
