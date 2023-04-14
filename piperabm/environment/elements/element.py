from piperabm.boundary import Point
from piperabm.unit import Date
from piperabm.degradation.sudden import SuddenDegradation
from piperabm.degradation.sudden.distributions import Eternal
from piperabm.degradation.progressive import ProgressiveDegradation
from piperabm.degradation.progressive.formulas import Formula_01


class Element:

    def __init__(
        self,
        boundary=None,
        active: bool=True,
        start_date: Date = None,
        end_date: Date = None,
        sudden_degradation_dist=None,
        sudden_degradation_coeff=None,
        progressive_degradation_formula=None,
        progressive_degradation_current=None,
        progressive_degradation_max=None,
    ):
        # boundary:
        if boundary is None:
            boundary = Point()
        self.boundary = boundary

        # activeness:
        self.active = active

        # dates:
        self.start_date = start_date
        self.end_date = end_date

        # sudden degradation:
        self.sudden_degradation = self.add_sudden_degradation(
            distribution=sudden_degradation_dist,
            coeff=sudden_degradation_coeff
        )

        # progressive degradation:
        self.progressive_degradation = self.add_progressive_degradation(
            formula=progressive_degradation_formula,
            current=progressive_degradation_current,
            max=progressive_degradation_max
        )

        # type:
        self.type = 'element'

    def add_progressive_degradation(
            self,
            formula=None,
            current=0,
            max=float('inf')
        ):
        if formula is None:
            formula = Formula_01
        progressive_degradation = ProgressiveDegradation(
            usage_max=max,
            usage_current=current,
            formula=formula
        )
        return progressive_degradation

    def add_sudden_degradation(self, distribution=None, coeff: float=1):
        if distribution is None:
            distribution = Eternal()
        if coeff is None:
            coeff = 1
        sudden_degradation = SuddenDegradation(
            initiation_date=self.start_date,
            distribution=distribution,
            coeff=coeff
        )
        return sudden_degradation

    def update(self, start_date: Date, end_date: Date):
        self.active = self.sudden_degradation_active(
            start_date=start_date,
            end_date=end_date
        )

    def add_usage(self, amount: float):
        self.progressive_degradation.add_usage(amount)

    def progressive_degradation_factor(self):
        return self.progressive_degradation.factor()

    def sudden_degradation_active(self, start_date: Date, end_date: Date):
        return self.sudden_degradation.is_active(
            start_date=start_date,
            end_date=end_date
        )


if __name__ == "__main__":
    element = Element()