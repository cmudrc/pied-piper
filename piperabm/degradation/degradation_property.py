import numpy as np


class SuddenDegradation:
    """
    Represent degradation property of an element that degrades by sudden.
    """
    def probability_of_working(self, initiation_date, distribution, start_date, end_date, coeff=1):
        """
        Probability of remaining active during the desired duration of time.
        
        Args:
            initiation_date: 
            distribution: 
            start_date: start of duration of time, datetime object
            end_date: end of duration of time, datetime object
            coeff: coefficient for adjusting probability based on its size
        """
        time_start = (start_date - initiation_date).total_seconds()
        time_end = (end_date - initiation_date).total_seconds()
        Q = distribution.probability(time_start, time_end)
        Q *= coeff
        if Q > 1: Q = 1
        elif Q < 0: Q = 1
        return 1 - Q

    def is_working(self, probability):
        """
        Check if the structure survived based on weighted random and returns the result (True/False).
        
        Args:
            probability: probability of working (or remaining alive) at each step
        
        """
        if probability > 1: probability = 1
        elif probability < 0: probability = 0
        sequence = [True, False]  # set of possible outcomes
        weights = [probability, 1-probability]
        index = np.random.choice(
            2, # np.arange(1)
            1, # return one element
            p=weights
        )
        return sequence[int(index)]

    def is_active(self, initiation_date, distribution, start_date, end_date, coeff=1):
        """
        Check if the element is going to survive the desired duration of time or not.

        Args:
            start_date: start of duration of time, datetime object
            end_date: end of duration of time, datetime object
        
        Returns:
            active (True/False)
        """
        probability = self.probability_of_working(initiation_date, distribution, start_date, end_date, coeff)
        active = self.is_working(probability)
        return active


class ProgressiveDegradation:
    """
    Represent degradation property of an element that degrades over time due to usage.
    """
    def progressive_degradation_factor(self, current_axels, total_axels):
        factor = 1 + (5 * current_axels/total_axels)
        return factor