from load_initial import model
from piperabm.time import DeltaTime


kwargs = {
    'max_time_outside': DeltaTime(minutes=5),
}

model.generate_agents(
    num=300,
    **kwargs
)

model.save_initial()
model.save_final()