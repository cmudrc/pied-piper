import os
from piperabm.model_new import Model


model = Model()
model.path = os.path.dirname(os.path.realpath(__file__))
model.animate()