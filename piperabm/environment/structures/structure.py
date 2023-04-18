from piperabm.unit import Date, date_to_dict, date_from_dict
from piperabm.object import Object
from piperabm.boundary import Point, Boundary
from piperabm.degradation.sudden import SuddenDegradation
from piperabm.degradation.sudden.distributions import Eternal
from piperabm.degradation.progressive import ProgressiveDegradation
from piperabm.degradation.progressive.formulas import Formula_01
from piperabm.tools import ElementExists


class Structure(Object):
    """
    Represent a physical element
    """

    def __init__(
        self,
        boundary=None,
        active: bool = True,
        start_date: Date = None,
        end_date: Date = None,
        sudden_degradation_dist=None,
        sudden_degradation_coeff: float=None,
        progressive_degradation_formula=None,
        progressive_degradation_current: float=None,
        progressive_degradation_max: float=None,
    ):
        super().__init__()

        # boundary:
        if boundary is None:
            shape = Point()
            boundary = Boundary(shape)
        self.boundary = boundary

        # activeness:
        self.active = active

        # dates:
        if start_date is None:
            start_date = Date.today()
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
        current: float = 0,
        max: float = float('inf')
    ):
        """
        Add progressive_degaradtion object
        """
        if formula is None:
            formula = Formula_01
        progressive_degradation = ProgressiveDegradation(
            usage_max=max,
            usage_current=current,
            formula=formula
        )
        return progressive_degradation

    def add_sudden_degradation(self, distribution=None, coeff: float = 1):
        """
        Add sudden_degaradtion object
        """
        if distribution is None:
            distribution = Eternal()
        if coeff is None:
            coeff = 1
        sudden_degradation = SuddenDegradation(
            distribution=distribution,
            coeff=coeff
        )
        return sudden_degradation

    def update(self, start_date: Date, end_date: Date):
        self.active = self.sudden_degradation_active(
            initiation_date=self.start_date,
            start_date=start_date,
            end_date=end_date
        )

    def repair(self, amount: float):
        """
        Add usage to progressive_degradation
        """
        self.progressive_degradation.repair(amount)

    def add_usage(self, amount: float):
        """
        Add usage to progressive_degradation
        """
        self.progressive_degradation.add_usage(amount)

    def degradation_factor(self):
        """
        Add usage to progressive_degradation
        """
        return self.progressive_degradation.factor()

    def degradation_active(self, start_date: Date, end_date: Date):
        """
        Check if the element is active based on sudden_degradation
        """
        return self.sudden_degradation.is_active(
            initiation_date=self.start_date,
            start_date=start_date,
            end_date=end_date
        )
    
    def exists(self, start_date: Date, end_date: Date):
        """
        Check whether element exists in the time range
        """
        ee = ElementExists()
        return ee.check(
            item_start=self.start_date,
            item_end=self.end_date,
            time_start=start_date,
            time_end=end_date
        )
    
    def to_dict(self) -> dict:
        return {
            'boundary': self.boundary.to_dict(),
            'active': self.active,
            'start_date': date_to_dict(self.start_date),
            'end_date': date_to_dict(self.end_date),
            'sudden_degradation': self.sudden_degradation.to_dict(),
            'progressive_degradation': self.progressive_degradation.to_dict(),
            'type': self.type
        }
    
    def from_dict(self, dictionary: dict) -> None:
        boundary = Boundary()
        boundary.from_dict(dictionary['boundary'])
        self.boundary = boundary
        self.active = dictionary['active']
        self.start_date = date_from_dict(dictionary['start_date'])
        self.end_date = date_from_dict(dictionary['end_date'])
        sudden_degradation = SuddenDegradation()
        sudden_degradation.from_dict(dictionary['sudden_degradation'])
        self.sudden_degradation = sudden_degradation
        progressive_degradation = ProgressiveDegradation()
        progressive_degradation.from_dict(dictionary['progressive_degradation'])
        self.progressive_degradation = progressive_degradation
        self.type = dictionary['type']


if __name__ == "__main__":
    structure = Structure()
    print(structure)
