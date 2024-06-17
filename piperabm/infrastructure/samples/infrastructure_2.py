from piperabm.model import Model


model = Model()
model.infrastructure.add_market(
    pos=[40, -40],
    name='market',
    id=0,
    food=100,
    water=100,
    energy=100
)
model.infrastructure.add_home(pos=[-60, 40], name='home 1', id=1)
model.infrastructure.add_home(pos=[200, 20], name='home 2', id=2)
model.infrastructure.add_home(pos=[100, -180], name='home 3', id=3)
model.infrastructure.add_street(pos_1=[-60, 40], pos_2=[0, 0], name='street 1', id=4)
model.infrastructure.add_street(pos_1=[0, 0], pos_2=[80, 60], name='street 2', id=5)
model.infrastructure.add_street(pos_1=[80, 60], pos_2=[200, 20], name='street 3', id=6)
model.infrastructure.add_street(pos_1=[0, 0], pos_2=[100, -180], name='street 4', id=7)
model.infrastructure.bake()


if __name__ == '__main__':
    model.infrastructure.show()
