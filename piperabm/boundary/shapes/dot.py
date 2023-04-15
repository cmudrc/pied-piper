from piperabm.boundary.shapes.circle import Circle
from piperabm.setting import SETTING


class Dot(Circle):

    def __init__(self):
        epsilon = SETTING['eps']
        super().__init__(radius=epsilon)
        self.type = 'dot'


if __name__ == "__main__":
    shape = Dot()
    print(shape)