from piperabm.boundery import Circular
from piperabm.tools import name_gen


class Cross:

    def __init__(
        self,
        pos=None,
        radius=1,
        all_cross=None
    ):
        self.boundery = Circular(radius)
        self.boundery.center = pos
        self.name = name_gen(all_cross, default_name='cross')

    def is_in(self, pos):
        return self.boundery.is_in(pos)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    all_cross = []
    c_1 = Cross(
        pos=[0, 0],
        all_cross=all_cross
    )
    all_cross.append(c_1)

    c_2 = Cross(
        pos=[10, 10],
        all_cross=all_cross
    )
    all_cross.append(c_2)

    print(c_1.name, c_2.name)