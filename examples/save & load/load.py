'''
This example loads the model from a save file
'''

import os

from piperabm.model import Model


path = os.path.dirname(os.path.realpath(__file__))
filename = 'sample'

new_model = Model()
new_model.load(path, filename)

#print(new_model)
new_model.show()
