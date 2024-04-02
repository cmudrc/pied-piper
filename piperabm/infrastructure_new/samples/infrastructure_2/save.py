import os

from piperabm.infrastructure_new import Infrastructure, Home, Street
    

infrastructure = Infrastructure()
infrastructure.path = os.path.dirname(os.path.realpath(__file__))

home_1 = Home(
    name='home 1',
    pos=[-60, 40]
)
home_2 = Home(
    name='home 2',
    pos=[200, 20]
)
home_3 = Home(
    name='home 3',
    pos=[100, -180]
)
street_1 = Street(
    name='street 1',
    pos_1=[-60, 40],
    pos_2=[0, 0]
)
street_2 = Street(
    name='street 2',
    pos_1=[0, 0],
    pos_2=[80, 60]
)
street_3 = Street(
    name='street 3',
    pos_1=[80, 60],
    pos_2=[200, 20]
)
street_4 = Street(
    name='street 4',
    pos_1=[0, 0],
    pos_2=[100, -180]
)
infrastructure.add(home_1, id=1)
infrastructure.add(home_2, id=2)
infrastructure.add(home_3, id=3)
infrastructure.add(street_1, id=4)
infrastructure.add(street_2, id=5)
infrastructure.add(street_3, id=6)
infrastructure.add(street_4, id=7)

infrastructure.bake(save=True, name='infrastructure_2')


if __name__ == '__main__':
    #infrastructure.save('infrastructure_2')
    #print(infrastructure)
    infrastructure.show()