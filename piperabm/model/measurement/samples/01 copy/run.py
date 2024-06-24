import os

from piperabm.society.samples.society_2 import model


model.path = os.path.dirname(os.path.realpath(__file__))
model.save(state='initial')
model.run(n=10, save=True, report=True)