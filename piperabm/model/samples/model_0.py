from piperabm.model import Model
from piperabm.infrastructure import Settlement
    

model = Model(
    proximity_radius=0.1,
    name='Sample Model 00',
    average_income=1000
)

settlement = Settlement(
    name='Sample Settlement',
    pos=[0, 0]
)
model.add(settlement)

#model.apply_grammars()


if __name__ == '__main__':
    print(model.infrastructure)
    pass
    #model.print
    #model.show()
