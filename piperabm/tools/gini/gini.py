from piperabm.tools.gini.gini_coefficient import gini_coefficient
from piperabm.tools.gini.gini_lognormal import GiniLogNormal


class gini:
    """
    A module to work with gini index
    """

    def coefficient(sample):
        """
        Calculate gini coefficient
        """
        return gini_coefficient(sample)
    
    def lognorm(gini_index: float = 0, average: float = 1):
        """
        Create a lognormal distribution by gini index and average
        """
        return GiniLogNormal(gini_index, average)
    

if __name__ == "__main__":
    
    from piperabm.tools.average import average as avg

    incomes = [100, 300, 500, 700, 900, 300, 500, 700, 500]
    gini_index = gini.coefficient(incomes)
    average = sum(incomes) / len(incomes)
    distribution = gini.lognorm(gini_index=gini_index, average=average)
    sample = distribution.rvs(sample_size=100, percision=0.02)
    print("Averages ratio: ", avg.arithmetic(values=sample) / avg.arithmetic(values=incomes))
    print("Gini index ratio: ", gini.coefficient(sample) / gini_index)