import os

from data.streets import streets
from examples.utqiavik.data.coordinates import coordinates
from create_model import create_model


path = os.path.dirname(os.path.realpath(__file__))
filename = 'utqiavik'

model = create_model(streets, coordinates)
model.apply_grammars()
model.name = filename
model.remove_save(path)
model.save(path)