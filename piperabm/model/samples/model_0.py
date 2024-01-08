from piperabm.model import Model
from piperabm.infrastructure import Settlement
    

model = Model(
    proximity_radius=0.1,
    name="Sample Model 00"
)

settlement = Settlement(
    name="Sample Settlement",
    pos=[0, 0]
)
model.add(settlement)


if __name__ == "__main__":
    #model.print
    model.show()
