from piperabm.asset import Use, Produce, Storage, Deficiency
from piperabm.asset import Resource, Asset
from piperabm.unit import Date, DT
from piperabm import Environment, Model, Agent

### Setup Environment
env = Environment(
    x_lim=[-150,150],
    y_lim=[-100,100],
)

### Setup Agent
food = Resource(
    name='food',
    use=Use(rate=0.2),
    produce=Produce(rate=0.1),
    storage=Storage(current_amount=5, max_amount=10),
    deficiency=Deficiency(current_amount=0, max_amount=10)
)
john = Agent(
    name='John',
    pos=[0,0],
    asset=Asset([food])
)

m = Model(
    environment=env,
    agents=[john],
    step_size=DT(seconds=10),
    current_step=0,
    current_date=Date(2000,1,1)
)

#m.agents[0].asset.show()
m.run(15)
m.agents[0].asset.show()
#print(m.agents[0].active)