import os

from piperabm.infrastructure_new import Infrastructure, Home
    

infrastructure = Infrastructure()
infrastructure.path = os.path.dirname(os.path.realpath(__file__))

home = Home(name='home', pos=[0, 0])
infrastructure.add(home, id=0)

infrastructure.bake(save=True, name='infrastructure_0')


if __name__ == '__main__':
    infrastructure.show()
