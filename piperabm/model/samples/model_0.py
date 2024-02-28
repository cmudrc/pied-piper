from piperabm.model import Model
from piperabm.infrastructure import Settlement
    

model = Model(proximity_radius=0.1)
settlement = Settlement(name='Sample Settlement', pos=[0, 0])
model.add(settlement)
model.bake(save=False)


if __name__ == '__main__':
    print(model.infrastructure)
    pass
    #model.print
    #model.show()
