import os

from piperabm.model_new import Model
from piperabm.infrastructure_new.samples import infrastructure_2 as infrastructure
from piperabm.society_new.samples import society_2 as society


model = Model(
    infrastructure=infrastructure,
    society=society,
)
model.path = os.path.dirname(os.path.realpath(__file__))