import os

from piperabm.model_new import Model
from piperabm.society_new import Society
from piperabm.infrastructure_new.samples import infrastructure_1 as infrastructure


society = Society()
model = Model(
    infrastructure=infrastructure,
    society=society,
)
model.path = os.path.dirname(os.path.realpath(__file__))
society.generate_agents(
    num=6,
    gini_index=0.3,
    average_balance=10,
    average_income=1000,
    average_resources={'food': 1, 'water': 1, 'energy': 1}
)
print(society.gini_index)
society.save(name='society_1')