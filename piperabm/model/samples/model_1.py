from piperabm.model import Model
from piperabm.infrastructure.items import Settlement, Road
    

model = Model(proximity_radius=0.1)
road = Road(pos_1=[0, 0], pos_2=[-60, 40], name="road")
settlement_1 = Settlement(pos=[5, 0], name="home 1")
settlement_1.id = 1
settlement_2 = Settlement(pos=[-60, 45], name="home 1")
settlement_2.id = 2
model.add(road, settlement_1, settlement_2)
model.bake(save=False)


if __name__ == '__main__':
    model.show()
