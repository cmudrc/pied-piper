from piperabm.environment.structures.structure import Structure
from piperabm.boundary import Rectangular
from piperabm.unit import Date


class LongStructure(Structure):

    def __init__(
        self,
        boundary=None,
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
        if boundary is None:
            boundary = Rectangular()
        if width is not None:
            boundary.shape.height = width
        super().__init__(
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

    def width(self):
        result = None
        boundary = self.boundary
        if boundary is not None:
            shape = boundary.shape
            if shape is not None:
                result = shape.height
        return result

    def length(self, mode='adjusted'):
        result = None
        if mode == 'adjusted':
            result = self._adjusted_length()
        elif mode == 'actual':
            result = self._actual_length()
        elif mode == 'ideal':
            result = self._ideal_length()
        return result

    def _actual_length(self):
        result = None
        actual_length = self.actual_length
        if actual_length is not None:
            result = actual_length
        return result
    
    def _ideal_length(self):
        result = None
        boundary = self.boundary
        if boundary is not None:
            result = boundary.shape.width
        return result
    
    def _adjusted_length(self):
        result = None
        degradation_factor = self.degradation_factor()
        if degradation_factor is None:
            degradation_factor = 1
        actual_length = self._actual_length()
        if actual_length is None:
            actual_length = self._ideal_length()
            if actual_length is None:
                actual_length = 1
        difficulty = self.difficulty
        if difficulty is None:
            difficulty = 1
        result = actual_length * difficulty * degradation_factor
        return result
    
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

