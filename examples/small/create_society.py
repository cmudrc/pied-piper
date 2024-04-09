import os

from load_infrastructure import infrastructure
from piperabm.model_new import Model


model = Model(infrastructure=infrastructure)
model.society.generate_agents(
    num=60,
    gini_index=0.3,
    average_balance=10,
    average_income=0.001,
)
model.society.path = os.path.dirname(os.path.realpath(__file__))
model.society.save()