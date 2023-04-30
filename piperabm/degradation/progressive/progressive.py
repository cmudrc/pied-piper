from piperabm.object import Object
from piperabm.degradation.progressive.formulas import load_formula
from piperabm.degradation.progressive.formulas.formula_01 import Formula as Formula_01
from piperabm.tools.symbols import SYMBOLS, serialize_symbol, deserialize_symbol


class ProgressiveDegradation(Object):
    """
    Represent degradation property of an element that degrades over time due to usage.
    """

    def __init__(
        self,
        usage_max: float=None,
        usage_current: float=None,
        formula=None
    ):
        super().__init__()
        if usage_current is None:
            usage_current = 0
        self.usage_current = usage_current
        if usage_max is None:
            usage_max = SYMBOLS['inf']
        self.usage_max = usage_max
        if formula is None:
            formula = Formula_01
        self.formula = formula

    def repair(self, amount: float=0):
        if self.usage_current is not None:
            self.usage_current -= amount

    def add_usage(self, amount: float=0):
        if self.usage_current is not None:
            self.usage_current += amount

    def ratio(self):
        result = None
        if self.usage_current is not None and \
            self.usage_max is not None:
            result = self.usage_current / self.usage_max
        if result is not None:
            if result < 0:
                result = 0
            elif result > 1:
                result = 1
        return result

    def factor(self):
        result = None
        if self.formula is not None:
            ratio = self.ratio()
            if ratio is not None:
                result = self.formula.calculate(ratio)
        return result
    
    def to_dict(self) -> dict:
        return {
            'usage_max': self.usage_max,
            'usage_current': self.usage_current,
            'formula_name': self.formula.name
        }
    
    def from_dict(self, dictionary: dict) -> None:
        usage_max = dictionary['usage_max']
        self.usage_max = usage_max
        current_usage = dictionary['usage_current']
        self.usage_current = current_usage
        self.formula = load_formula(dictionary['formula_name'])
    

if __name__ == "__main__":
    degradation = ProgressiveDegradation(
        usage_current=3,
        usage_max=10
    )
    print(degradation.factor())
    print(degradation)
