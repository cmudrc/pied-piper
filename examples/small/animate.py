import os

from load import model


model.path = os.path.dirname(os.path.realpath(__file__))
model.animate()