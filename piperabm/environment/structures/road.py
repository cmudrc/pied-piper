from piperabm.environment.structures.structure import Structure
from piperabm.unit import Date
from piperabm.boundary.rectangular import Rectangular


class Road(Structure):

    def __init__(
        self,
        boundary=None,
        active=True,
        start_date: Date = None,
        end_date: Date = None,
        sudden_degradation_dist=None,
        sudden_degradation_coeff: float=None,
        progressive_degradation_formula=None,
        progressive_degradation_current: float=None,
        progressive_degradation_max: float=None
    ):
        if boundary is None:
            boundary = Rectangular()
        super().__init__(
            boundary=boundary,
            active=active,
            start_date=start_date,
            end_date=end_date,
            sudden_degradation_dist=sudden_degradation_dist,
            sudden_degradation_coeff=sudden_degradation_coeff,
            progressive_degradation_formula=progressive_degradation_formula,
            progressive_degradation_current=progressive_degradation_current,
            progressive_degradation_max=progressive_degradation_max
        )
        self.type = 'road'


if __name__ == "__main__":
    settlement = Road()