import os

from piperabm.model import Model


path = os.path.dirname(os.path.realpath(__file__))
filename = 'utqiavik_small'

model = Model()
model.load(path, filename)
model.show()