import os

from piperabm.infrastructure_new import Infrastructure
    

infrastructure = Infrastructure()
infrastructure.path = os.path.dirname(os.path.realpath(__file__))
infrastructure.load('infrastructure_0')


if __name__ == '__main__':
    infrastructure.show()
