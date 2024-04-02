from piperabm.model_new import Model
from piperabm.society_new import Society
from piperabm.infrastructure_new.samples import infrastructure_1 as infrastructure


society = Society()

model = Model(
    infrastructure=infrastructure,
    society=society,
    gini_index=0.3,
)