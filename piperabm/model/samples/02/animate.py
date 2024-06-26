import os

import piperabm as pa


name = 'model'
path = os.path.dirname(os.path.realpath(__file__))
model = pa.Model(name=name, path=path)
model.animate()