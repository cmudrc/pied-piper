from piperabm.environment import Environment
from piperabm.environment.items import Settlement, Road
    

environment = Environment(
    proximity_radius=1
)

settlement_1 = Settlement(
    name='Settlement 1',
    pos=[-60, 40]
)
environment.add(settlement_1)

settlement_2 = Settlement(
    name='Settlement 2',
    pos=[200, 20]
)
environment.add(settlement_2)

settlement_3 = Settlement(
    name='Settlement 3',
    pos=[100, -180]
)
environment.add(settlement_3)

road_1 = Road(
    name='Road 1',
    pos_1=[-60, 40],
    pos_2=[0, 0]
)
environment.add(road_1)

road_2 = Road(
    name='Road 2',
    pos_1=[0, 0],
    pos_2=[80, 60]
)
environment.add(road_2)

road_3 = Road(
    name='Road 3',
    pos_1=[80, 60],
    pos_2=[200, 20]
)
environment.add(road_3)

road_4 = Road(
    name='Road 4',
    pos_1=[0, 0],
    pos_2=[100, -180]
)
environment.add(road_4)

environment.apply_grammars()


if __name__ == '__main__':
    environment.show()