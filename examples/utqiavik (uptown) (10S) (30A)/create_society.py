from load_initial import model
from data.info import agents_num
from piperabm.time import DeltaTime


kwargs = {
    'max_time_outside': DeltaTime(minutes=5),
}

model.generate_agents(
    num=agents_num,
    **kwargs
)

model.save_initial()
model.save_final()