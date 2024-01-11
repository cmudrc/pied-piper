import os


path = os.path.dirname(os.path.realpath(__file__))
filename = 'utqiavik'

# Load
from piperabm.model import Model

model = Model()
model.load(path, filename)
model.show()