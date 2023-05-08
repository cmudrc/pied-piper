from piperabm import Environment
from piperabm.unit import Date, DT


env = Environment(links_unit_length=10)

env.add_settlement(name="Settlement 1", pos=[-60, 40], initiation_date=Date(2020, 1, 3))
env.add_settlement(name="Settlement 2", pos=[200, 20], initiation_date=Date(2020, 1, 1))
env.add_settlement(name="Settlement 3", pos=[100, -180], initiation_date=Date(2020, 1, 1))
env.add_link(start="Settlement 1", end=[0, 0], initiation_date=Date(2020, 1, 1))
env.add_link(start=[0.1, 0.1], end=[80, 60], initiation_date=Date(2020, 1, 1))
env.add_link(start=[80, 60], end=[200, 20], initiation_date=Date(2020, 1, 1))
env.add_link(start=[0, 0], end="Settlement 3", initiation_date=Date(2020, 1, 1))


if __name__ == "__main__":
    start_date = Date(2020, 1, 1)
    end_date = start_date + DT(hours=12)
    env.show(start_date, end_date)
    env.show(start_date, end_date, graph='path')