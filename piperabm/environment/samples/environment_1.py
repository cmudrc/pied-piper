from piperabm.environment import Environment
from piperabm.environment.items import Junction, Settlement, Road
from piperabm.time import Date
    

environment = Environment(
    proximity_radius=0.1
)

junction = Junction(
    name='Sample Junction',
    pos=[0, 0]
)
environment.add(junction)

settlement = Settlement(
    name='Sample Settlement',
    pos=[2, 2]
)
environment.add(settlement)

road = Road(
    name='Sample Road',
    pos_1=[0.05, 0],
    pos_2=[2, 2]
)
environment.add(road)

environment.apply_grammars()


if __name__ == '__main__':
    environment.show()
