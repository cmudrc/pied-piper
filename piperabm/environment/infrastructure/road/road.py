from piperabm.environment.infrastructure.objects import LongStructure
from piperabm.unit import Date


class Road(LongStructure):

    def __init__(
        self,
        name: str = '',
        active=True,
        start_date: Date = None,
        end_date: Date = None,
        actual_length: float = None,
        width: float = None,
        difficulty: float = 1,
        sudden_degradation_dist=None,
        sudden_degradation_unit_size: float=None,
        progressive_degradation_formula=None,
        progressive_degradation_current: float=None,
        progressive_degradation_max: float=None
    ):
        super().__init__(
            name=name,
            active=active,
            start_date=start_date,
            end_date=end_date,
            actual_length=actual_length,
            width=width,
            difficulty=difficulty,
            sudden_degradation_dist=sudden_degradation_dist,
            sudden_degradation_unit_size=sudden_degradation_unit_size,
            progressive_degradation_formula=progressive_degradation_formula,
            progressive_degradation_current=progressive_degradation_current,
            progressive_degradation_max=progressive_degradation_max
        )
        self.type = 'road'


if __name__ == "__main__":
    road = Road()
    print(road)