from piperabm.degradation.progressive.formulas.formula_00 import Formula as Formula_00
from piperabm.degradation.progressive.formulas.formula_01 import Formula as Formula_01
from piperabm.degradation.progressive.formulas.formula_02 import Formula as Formula_02


def load_formula(name: str):
    if name is None:
        formula = None
    else:
        if name == 'formula_00':
            formula = Formula_00
        elif name == 'formula_01':
            formula = Formula_01
        elif name == 'formula_02':
            formula = Formula_02
    return formula