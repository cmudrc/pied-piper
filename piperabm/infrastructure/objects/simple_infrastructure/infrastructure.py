from piperabm.object import Object
from piperabm.unit import Date, date_to_dict, date_from_dict
from piperabm.boundary import Point, Boundary
from piperabm.degradation.sudden import SuddenDegradation
from piperabm.degradation.sudden.distributions import Eternal
from piperabm.degradation.progressive import ProgressiveDegradation
from piperabm.degradation.progressive.formulas import Formula_01
from piperabm.tools import ElementExists


class Infrastructure(Object):
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
        sudden_degradation_unit_size: float = None,
        progressive_degradation_formula=None,
        progressive_degradation_current: float = None,
        progressive_degradation_max: float = None
    ):
        super().__init__()

        ''' identity '''
        self.name = name
        self.active = active
        self.type = 'infrastructure'

        if start_date is None:
            start_date = Date.today()
        self.start_date = start_date
        self.end_date = end_date

        ''' boundary '''
        if boundary is None:
            boundary = Point()
        self.boundary = boundary

        ''' sudden degradation '''
        self.sudden_degradation = self.add_sudden_degradation(
            distribution=sudden_degradation_dist,
            unit_size=sudden_degradation_unit_size
        )

        ''' progressive degradation '''
        self.progressive_degradation = self.add_progressive_degradation(
            formula=progressive_degradation_formula,
            current=progressive_degradation_current,
            max=progressive_degradation_max
        )

    def add_progressive_degradation(
        self,
        formula=None,
        current: float = 0,
        max: float = float('inf')
    ):
        """
        Add object to self.progressive_degaradtion
        """
        if formula is None:
            formula = Formula_01
        progressive_degradation = ProgressiveDegradation(
            usage_max=max,
            usage_current=current,
            formula=formula
        )
        return progressive_degradation

    def add_sudden_degradation(self, distribution=None, unit_size: float = None):
        """
        Add sudden_degaradtion object
        """
        if distribution is None:
            distribution = Eternal()
        sudden_degradation = SuddenDegradation(
            distribution=distribution,
            unit_size=unit_size
        )
        return sudden_degradation

    def update(self, start_date: Date, end_date: Date):
        """
        Update object
        """
        if self.active is True and \
            self.exists(start_date, end_date):

            ''' sudden degradation '''
            active = self.degradation_active(start_date, end_date)
            if active is False: # suddenly degraded
                self.active = active # update value

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

    def degradation_active(self, start_date: Date, end_date: Date, adjust_for_size: bool = False):
        """
        Check if the element is active based on sudden_degradation
        """
        size = None
        if adjust_for_size is True:
            size = self.size()
        return self.sudden_degradation.is_active(
            initiation_date=self.start_date,
            start_date=start_date,
            end_date=end_date,
            size=size
        )
    
    def size(self):
        return self.boundary.shape.size()

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
    
    def is_in(self, pos: list, center: list=None, local: bool=True) -> bool:
        result = None
        boundary = self.boundary
        if boundary is not None:
            if local:
                result = boundary.is_in(pos, center=[0, 0])
            else:
                if center is None or not isinstance(center, list):
                    raise ValueError
                result = boundary.is_in(pos, center=center)
        return result
    
    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'boundary': self.boundary.to_dict(),
            'active': self.active,
            'start_date': date_to_dict(self.start_date),
            'end_date': date_to_dict(self.end_date),
            'sudden_degradation': self.sudden_degradation.to_dict(),
            'progressive_degradation': self.progressive_degradation.to_dict(),
            'type': self.type
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.name = dictionary['name']
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
    object = Object()
    print(object)
