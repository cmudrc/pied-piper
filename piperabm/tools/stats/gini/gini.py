from piperabm.tools.stats.gini.gini_coefficient import gini_coefficient
from piperabm.tools.stats.gini.gini_lognormal import GiniLogNormal


class gini:

    def coefficient(sample):
        return gini_coefficient(sample)
    
    def lognorm(gini_index: float = 0, average: float = 1):
        return GiniLogNormal(gini_index, average)