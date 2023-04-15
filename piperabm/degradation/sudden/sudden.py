import numpy as np

from piperabm.object import Object
from piperabm.unit import Date
from piperabm.degradation.sudden.distributions import Eternal
from piperabm.degradation.sudden.distributions.load import load_sudden_degradation_distribution


class SuddenDegradation(Object):
    """
    Represent degradation property of an element that degrades by sudden.
    """

    def __init__(self, distribution=None, coeff: float=1):
        super().__init__()
        if distribution is None:
            distribution = Eternal()
        self.distribution = distribution
        self.coeff = coeff

    def date_to_time(
            self,
            initiation_date: Date,
            start_date: Date,
            end_date: Date
        ):
        time_start = (start_date - initiation_date).total_seconds()
        time_end = (end_date - initiation_date).total_seconds()
        return time_start, time_end

    def probability_of_working(self, time_start, time_end) -> float:
        """
        Calculate probability of staying active during the specified duration of time
        """

        probability_of_death = self.distribution.probability(
            time_start,
            time_end
        )
        probability_of_death *= self.coeff
        if probability_of_death > 1:
            probability_of_death = 1
        elif probability_of_death < 0:
            probability_of_death = 0
        return 1 - probability_of_death

    def is_working(self, probability: float) -> bool:
        """
        Check if the structure survived based on weighted random
        """
        if probability > 1: probability = 1
        elif probability < 0: probability = 0
        possible_outcomes = [True, False]  # set of possible outcomes
        weights = [probability, 1-probability]
        index = np.random.choice(
            a=2, # np.arange(1)
            size=1,
            p=weights
        )
        choice = possible_outcomes[int(index)]
        return choice

    def is_active(
            self,
            initiation_date: Date,
            start_date: Date,
            end_date: Date
        ) -> bool:
        """
        Check if the element is going to survive the desired duration of time or not
        """
        time_start, time_end = self.date_to_time(
            initiation_date,
            start_date,
            end_date
        )
        probability = self.probability_of_working(time_start, time_end)
        active = self.is_working(probability)
        return active

    def to_dict(self) -> dict:
        return {
            'distribution': self.distribution.to_dict(),
            'coeff': self.coeff,
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.distribution = load_sudden_degradation_distribution(dictionary['distribution'])
        self.coeff = dictionary['coeff']
    

if __name__ == "__main__":
    from piperabm.degradation.sudden.distributions import DiracDelta
    from piperabm.unit import DT

    distribution = DiracDelta(
        main=DT(days=5)
    )
    degradation = SuddenDegradation(
        distribution=distribution,
        coeff=1
    )
    active = degradation.is_active(
        initiation_date=Date(2020, 1, 1),
        start_date=Date(2020, 1, 2),
        end_date=Date(2020, 1, 4)
    )
    print(active)