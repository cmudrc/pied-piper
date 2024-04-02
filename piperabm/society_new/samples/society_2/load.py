import os

from piperabm.infrastructure_new.samples import infrastructure_2 as infrastructure
from piperabm.society_new import Society


society = Society()
society.path = os.path.dirname(os.path.realpath(__file__))
society.load(name='society_2')

#print(society.gini_index)