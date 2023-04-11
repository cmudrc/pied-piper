from piperabm.boundary import Point
from piperabm.degradation.sudden.distributions import Eternal


class Element:

    def __init__(
        self,
        boundary=None,
        active=True,
        sudden_degradation=None,
        progressive_degradation=None
    ):
        # boundary:
        if boundary is None:
            boundary = Point()
        self.boundary = boundary

        # activeness:
        self.active = active

        # sudden degradation:
        if sudden_degradation is None:
            sudden_degradation = Eternal()
        self.sudden_degradation = sudden_degradation

        # progressive degradation:
        if progressive_degradation is None:
            progressive_degradation = None #########
        self.progressive_degradation = progressive_degradation

        # type:
        self.type = 'element'


if __name__ == "__main__":
    element = Element()