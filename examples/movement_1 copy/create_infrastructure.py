import os

from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement
from piperabm.matter import Containers, Matter
from piperabm.time import Date, DeltaTime


""" Setup model """
id_agent = 0
id_start = 1
id_end = 2
pos_start = [0, 0]
pos_end = [5000, 0]
average_resources = Containers(
    Matter('food', 0.2),
    Matter('water', 0.2),
    Matter('energy', 0.2)
)
model = Model(
    proximity_radius=1,  # Meters
    step_size=DeltaTime(seconds=100),  # Seconds
    current_date=Date(2000, 1, 1),
    average_income=100,  # Dollars per month
    average_resources=average_resources,
    name="Sample Model",
    path=os.path.dirname(os.path.realpath(__file__)),
)
road = Road(
    pos_1=pos_start,
    pos_2=pos_end,
    roughness=2
)
settlement_1 = Settlement(pos=pos_start, name="start")
settlement_1.id = id_start
settlement_2 = Settlement(pos=pos_end, name="end")
settlement_2.id = id_end
model.add(road, settlement_1, settlement_2)
model.bake(save=True)