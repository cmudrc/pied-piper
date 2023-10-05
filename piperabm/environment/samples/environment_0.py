from piperabm.environment import Environment
from piperabm.environment.items import Settlement
from piperabm.time import Date
    

environment = Environment(
    proximity_radius=0.1
)

settlement = Settlement(
    name="Sample Settlement",
    pos=[0, 0]
)
environment.add(settlement)


if __name__ == '__main__':
    environment.show()
