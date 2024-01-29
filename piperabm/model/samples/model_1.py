from piperabm.model import Model
from piperabm.infrastructure.items import Junction, Settlement, Road
    

model = Model(
    proximity_radius=0.1
)

junction = Junction(
    name='Sample Junction',
    pos=[0, 0]
)
model.add(junction)

settlement = Settlement(
    name='Sample Settlement',
    pos=[-60, 40]
)
model.add(settlement)

road = Road(
    name='Sample Road',
    pos_1=[0.05, 0],
    pos_2=[-60, 40.05]
)
model.add(road)

model.apply_grammars()


if __name__ == '__main__':
    #model.print
    model.show()
