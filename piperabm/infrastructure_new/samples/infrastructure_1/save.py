import os

from piperabm.infrastructure_new import Infrastructure, Home, Street
    

infrastructure = Infrastructure()
infrastructure.path = os.path.dirname(os.path.realpath(__file__))

street = Street(pos_1=[0, 0], pos_2=[-60, 40], name="road")
home_1 = Home(pos=[5, 0], name="home 1")
home_2 = Home(pos=[-60, 45], name="home 1")
infrastructure.add(street, id=0)
infrastructure.add(home_1, id=1)
infrastructure.add(home_2, id=2)

infrastructure.bake()


if __name__ == '__main__':
    infrastructure.save('infrastructure_1')
    #print(infrastructure)
    infrastructure.show()
