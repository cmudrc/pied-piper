from piperabm.environment.infrastructure.objects.object import StructuralObject
from piperabm.unit import Date


class Structure(StructuralObject):
    """
    Represent a physical element
    """

    def __init__(
        self,
        name: str = '',
        boundary=None,
        active: bool = True,
        start_date: Date = None,
        end_date: Date = None,
        sudden_degradation_dist=None,
        sudden_degradation_unit_size: float=None,
        progressive_degradation_formula=None,
        progressive_degradation_current: float=None,
        progressive_degradation_max: float=None
    ):
        super().__init__(
            name=name,
            boundary=boundary,
            active=active,
            start_date=start_date,
            end_date=end_date,
            sudden_degradation_dist=sudden_degradation_dist,
            sudden_degradation_unit_size=sudden_degradation_unit_size,
            progressive_degradation_formula=progressive_degradation_formula,
            progressive_degradation_current=progressive_degradation_current,
            progressive_degradation_max=progressive_degradation_max
        )

        # type:
        self.type = 'structure'


if __name__ == "__main__":
    structure = Structure()
    print(structure)
