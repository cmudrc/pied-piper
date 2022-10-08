import random

from utils.unit_manager import Unit
from utils.statistic import Gaussian, DiracDelta


class DegradationProperty:
    """
    Represents degradation property of an object that degrades over time.

    Args:
        name: name
        active: is the object still active?
        initial_cost: cost of building the structure
        distribution: a dictionary containing information about the districbution function of life expectency
        seed: for repeatable results

    """
    def __init__(
        self,
        name=None,
        active=True,
        initial_cost=None,
        initiation_date=None,
        distribution=None,
        seed=None
    ):
        self.name = name
        self.active = active
        self.initial_cost = initial_cost
        self.renovation_effect = None
        self.initiation_date = initiation_date
        self.seed = seed

        if distribution is not None:
            if distribution['type'] == 'gaussian':
                self.distribution = Gaussian(
                    mean=distribution['mean'],
                    sigma=distribution['sigma']
                )
            elif distribution['type'] == 'dirac delta':
                self.distribution = DiracDelta(
                    main=distribution['main']
                )
    
    def renovation_effect_calc(self, renovation_cost, current_date):
        delta_t = (current_date - self.initiation_date)
        return delta_t * (renovation_cost / self.initial_cost)

    def probability_of_working(self, start_date, end_date):
        """
        Probability of remaining active during the desired duration of time.
        
        Args:
            start_date: start of duration of time, datetime object
            end_date: end of duration of time, datetime object
        
        """
        if self.distribution is not None:
            t0 = self.initiation_date
            t1 = start_date
            t2 = end_date

            Q = self.distribution.probability(
                time_start=Unit((t1-t0).days, 'day'),
                time_end=Unit((t2-t0).days, 'day')
            )
            P = 1 - Q
        else:
            P = 1
        return P

    def is_working(self, probability):
        """
        Checks if the structure survived based on weighted random.
        
        Args:
            probability: probability of working (or remaining alive) at each step
        
        """
        sequence = [True, False]  # set of possible outcomes
        if self.active is True:  # if is (still) active
            if self.seed is not None:
                random.seed(self.seed)  # if has seed
            result = random.choices(
                sequence,
                weights=[probability, 1-probability],
                k=1  # result length
            )
        else:
            result = False
        return result

    def show_distribution(self):
        """
        Shows the distribution

        """
        self.distribution.show()


if __name__ == "__main__":
    from datetime import date
    from utils.unit_manager import Unit


    s = DegradationProperty(
        name='sample structure',
        initiation_date=date(2000, 1, 1),
        distribution={
            'type': 'gaussian',
            'sigma': Unit(20,'day'),
            'mean': Unit(100,'day'),
        },
        seed=None
    )

    #P = s.probability_of_working(
    #    start_date=date(2000, 1, 1),
    #    end_date=Unit(100, 'day')+date(2000, 1, 1)
    #)
    #print(P)

    #print(s.is_working(P))

    #s.show_distribution()


    d = DegradationProperty(
        name='sample structure',
        initiation_date=date(2000, 1, 1),
        distribution={
            'type': 'dirac delta',
            'main': Unit(70,'day'),
        },
        seed=202
    )

    P = d.probability_of_working(
        start_date=Unit(0, 'day')+date(2000, 1, 1),
        end_date=Unit(50, 'day')+date(2000, 1, 1)
    )

    print(P)

    #print(s.is_working(P))

    #s.show_distribution()