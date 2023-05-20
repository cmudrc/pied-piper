from piperabm.infrastructure.objects.object import StructuralObject
from piperabm.infrastructure.objects.edge.track import Track
from piperabm.boundary import Rectangular
from piperabm.unit import Date


class LongStructure(StructuralObject, Track):

    def __init__(
        self,
        name: str = '',
        active: bool = True,
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
        boundary = Rectangular(height=width)
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
        self.actual_length = actual_length
        self.difficulty = difficulty
        self.type = 'long structure'

    def width(self):
        """
        Return width of the long structure (e.g. road)
        """
        result = None
        boundary = self.boundary
        if boundary is not None:
            shape = boundary.shape
            if shape is not None:
                result = shape.height
        return result

    @property
    def angle(self):
        result = None
        boundary = self.boundary
        if boundary is not None:
            shape = boundary.shape
            if shape is not None:
                result = shape.angle
        return result

    def length(self, mode='adjusted'):
        """
        Return distance between start and end points
        """
        result = None
        if mode == 'adjusted':
            result = self._adjusted_length()
        elif mode == 'actual':
            result = self._actual_length()
        elif mode == 'ideal':
            result = self._ideal_length()
        return result
    
    def area(self, mode='adjusted'):
        """
        Return surface area of long structure between start and end points,
        useful for calculating adjusted degradation probability
        """
        result = None
        if self.boundary is not None:
            length = self.length(mode)
            width = self.boundary.shape.height
            result = length * width
        return result

    def _actual_length(self):
        """
        Return actual distance between start and end points,
        useful while reading real-world data
        """
        result = None
        actual_length = self.actual_length
        if actual_length is not None:
            result = actual_length
        return result
    
    def _ideal_length(self):
        """
        Return euclidean distance between start and end points,
        useful for visualizations
        """
        result = None
        boundary = self.boundary
        if boundary is not None:
            result = boundary.shape.width
        return result
    
    def _adjusted_length(self):
        """
        Return adjusted distance between start and end points,
        useful for calculations related to transportation
        """
        ''' progressive degradation factor '''
        degradation_factor = self.degradation_factor()
        if degradation_factor is None:
            degradation_factor = 1
        ''' euclidean distance '''
        actual_length = self._actual_length()
        if actual_length is None:
            actual_length = self._ideal_length()
            if actual_length is None:
                actual_length = 0
        ''' difficulty coefficient '''
        difficulty = self.difficulty
        if difficulty is None:
            difficulty = 1
        ''' main '''
        return actual_length * difficulty * degradation_factor

    def to_dict(self) -> dict:
        dictionary = super().to_dict()
        dictionary['actual_length'] = self.actual_length
        dictionary['difficulty'] = self.difficulty
        return dictionary

    def from_dict(self, dictionary: dict) -> None:
        super().from_dict(dictionary)
        self.actual_length = dictionary['actual_length']
        self.difficulty = dictionary['difficulty']
    

if __name__ == "__main__":
    structure = LongStructure()
    print(structure)

