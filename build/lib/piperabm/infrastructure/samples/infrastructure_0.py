from piperabm.model import Model


model = Model()
model.infrastructure.add_home(pos=[0, 0], id=0, name='home')
model.infrastructure.bake()


if __name__ == '__main__':
    model.infrastructure.show()
