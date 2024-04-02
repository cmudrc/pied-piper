from piperabm.model_new import Model
from piperabm.society_new import Society
from infrastructure_1 import infrastructure


society = Society()
model = Model(
    infrastructure=infrastructure,
    society=society,
)
society.generate_agents(num=6)