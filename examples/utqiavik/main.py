import os


path = os.path.dirname(os.path.realpath(__file__))
filename = 'utqiavik'

# Save
'''
from streets import streets
from labels import labels
from load import load

model = load(streets, labels)
model.apply_grammars()
model.name = filename
model.save(path)
'''

# Load
from piperabm.model import Model

model = Model()
model.load(path, filename)
model.show()