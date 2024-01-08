import os

from piperabm.model.samples import model_0 as model

path = os.path.dirname(os.path.realpath(__file__))
model.save(path)