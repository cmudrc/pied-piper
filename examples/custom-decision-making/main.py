"""
In this example, we see how the user can customize decision-making behavior of the agents in the model by providing their own `decision_making.py` file.
"""
import os

import piperabm as pa


path = os.path.dirname(os.path.realpath(__file__))
model = pa.Model(path=path, seed=2)

# Set up the infrastructure
model.infrastructure.coeff_usage = 1
model.infrastructure.coeff_age = 1
model.infrastructure.add_street(pos_1=[0, 0], pos_2=[-60, 40], name='road')
model.infrastructure.add_home(pos=[5, 0], id=1, name='home')
model.infrastructure.add_market(
    pos=[-60, 45],
    id=2,
    name='market',
    resources={'food': 100, 'water': 100, 'energy': 100,}
)
model.infrastructure.bake()

# Set up the society
model.society.average_income = 1
agent_id = 1
home_id = model.infrastructure.homes[0]
model.society.add_agent(
    id=agent_id,
    home_id=home_id,
    socioeconomic_status=1,
    resources={"food": 1, "water": 1, "energy": 1,},
    balance=100
)

# Run the simulation
model.run(n=80, step_size=1, save=True)

# Animate the result
model.animate()