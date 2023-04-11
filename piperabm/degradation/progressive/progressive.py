from piperabm.degradation.progressive.formulas import load_formula
from piperabm.degradation.progressive.formulas.formula_01 import Formula as Formula_01


class ProgressiveDegradation:
    """
    Represent degradation property of an element that degrades over time due to usage.
    """

    def __init__(
        self,
        usage_max: float=None,
        usage_current: float=0,
        formula=None
    ):
        self.usage_current = usage_current
        self.usage_max = usage_max
        if formula is None:
            formula = Formula_01
        self.formula = formula

    def add_usage(self, amount: float):
        self.usage_current += amount

    def ratio(self):
        result = None
        if self.usage_current is not None and \
            self.usage_max is not None:
            result = self.usage_current / self.usage_max
        return result

    def factor(self):
        result = None
        if self.formula is not None:
            result = self.formula.calculate(ratio=self.ratio())
        return result
    
    def to_dict(self) -> dict:
        return {
            'usage_max': self.usage_max,
            'usage_current': self.usage_current,
            'formula_name': self.formula.name
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.usage_max = dictionary['usage_max']
        self.usage_current = dictionary['usage_current']
        self.formula = load_formula(dictionary['formula_name'])

    def __eq__(self, other):
        result = False
        if self.ratio() == other.ratio() and \
            self.formula.name == other.formula.name:
            result = True
        return result
    

if __name__ == "__main__":
    degradation = ProgressiveDegradation(
        usage_max=10,
        usage_current=3
    )
    print(degradation.factor())