from piperabm import Model, Environment
from piperabm.unit import Date, DT


env = Environment(links_unit_length=10)

env.add_settlement(
    name="Settlement 1",
    pos=[-50, 0]
)
env.add_settlement(
    name="Settlement 2",
    pos=[50, 0]
)