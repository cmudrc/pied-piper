from piperabm import Environment
from piperabm.unit import Date, DT

env = Environment(links_unit_length=10)
env.add_settlement(name="Settlement 1", pos=[-60, 40])
env.add_settlement(name="Settlement 2", pos=[200, 20])
env.add_settlement(name="Settlement 3", pos=[100, -180])
env.add_link(start="Settlement 1", end=[0, 0])
env.add_link(start=[0.1, 0.1], end=[80, 60])
env.add_link(start=[80, 60], end=[200, 20])
env.add_link(start=[0, 0], end="Settlement 3")

start_date = Date.today()
end_date = start_date + DT(days=1)
env.show(start_date, end_date)