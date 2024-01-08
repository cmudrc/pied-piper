from piperabm.model import Model
from piperabm.infrastructure.items import Settlement, Market, Road
    

model = Model(
    proximity_radius=1
)

settlement_1 = Settlement(
    name='Settlement 1',
    pos=[-22, 10]
)
settlement_2 = Settlement(
    name='Settlement 2',
    pos=[19.5, 0]
)
settlement_3 = Settlement(
    name='Settlement 3',
    pos=[0.1, -12.8]
)
model.add(settlement_1, settlement_2, settlement_3)

road_1 = Road(
    name='Road 1',
    pos_1=[-20, 10.2],
    pos_2=[-19.8, 0.5]
)
road_2 = Road(
    name='Road 2',
    pos_1=[-20.1, 0],
    pos_2=[20, 0.1]
)
road_3 = Road(
    name='Road 3',
    pos_1=[0, 10.3],
    pos_2=[-0.1, 0]
)
road_4 = Road(
    name='Road 4',
    pos_1=[0, 0],
    pos_2=[0, -10]
)
model.add(road_1, road_2, road_3, road_4)

market_1 = Market(
    name='Market 1',
    pos=[0, 10]
)
model.add(market_1)


if __name__ == '__main__':
    #model.print
    model.show()