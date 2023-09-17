from piperabm.environment import Environment
from piperabm.environment.items import Junction, Settlement, Road
from piperabm.time import Date
    

environment = Environment()

junction = Junction(
    name='Sample Junction',
    pos=[0, 0]
)
environment.add(junction)

settlement = Settlement(
    name='Sample Settlement',
    pos=[2, 2],
    date_start=Date(2020, 1, 1)
)
environment.add(settlement)

road = Road(
    pos_1=[0.05, 0],
    pos_2=[2, 2],
    name='sample road'
)
environment.add(road)


if __name__ == "__main__":
    environment.print
