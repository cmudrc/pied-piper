from piperabm.tools.shapes.circle import Circle
from piperabm.tools.symbols import SYMBOLS


class Dot(Circle):

    def __init__(self):
        epsilon = SYMBOLS['eps']
        super().__init__(radius=epsilon)
        self.type = 'dot'


if __name__ == "__main__":
    shape = Dot()
    print(shape)