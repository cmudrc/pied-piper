from piperabm.tools.average.arithmetic import arithmetic
from piperabm.tools.average.geometric import geometric


class average:

    def arithmetic(values: list, weights: list = None):
        return arithmetic(values=values, weights=weights)
    
    def geometric(values: list, weights: list = None):
        return geometric(values=values, weights=weights)