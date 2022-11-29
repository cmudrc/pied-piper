from piperabm.boundery import Circular


class Cross:

    def __init__(
        self,
        pos=None,
        radius=1
    ):
        self.boundery = Circular(radius)
        self.boundery.center = pos
        