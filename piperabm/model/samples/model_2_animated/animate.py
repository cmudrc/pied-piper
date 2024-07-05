import os

import piperabm as pa


path = os.path.dirname(os.path.realpath(__file__))
model = pa.Model(path=path)
model.animate()