import os


path = os.path.dirname(os.path.realpath(__file__))
filename = 'utqiavik'

# Save
from data.streets import streets
from data.labels import labels
from create_model import create_model

model = create_model(streets, labels)
model.apply_grammars()
model.name = filename
model.remove_save(path)
model.save(path)