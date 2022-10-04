from tools.statistics import Gaussian
import random


class DegradationProperty():
    '''
    Represents a structure that degrades over time

    '''

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
        self.initiation_date = initiation_date
        self.renovation_effect = None
        self.seed = seed

        if distribution is not None:
            if distribution['type'] == 'gaussian':
                self.distribution = Gaussian(
                    mean=distribution['mean'],
                    sigma=distribution['sigma']
                )

    def probability_of_working(self, start_date, end_date):
        '''
        Probability of working in the desired duration of time
        
        Args:
            start_date: start of duration of time, datetime object
            end_date: end of duration of time, datetime object
        '''
        if self.distribution is not None:
            t0 = self.initiation_date
            t1 = start_date
            t2 = end_date

            Q = self.distribution.probability(
                time_start=t1-t0,
                time_end=t2-t0
            )
            P = 1 - Q
        else:
            P = 1
        return P

    def is_working(self, probability):
        '''
        Checks if the structure survived based on weighted random.
        
        Args:
            probability: probability of working (or remaining alive) at each step
        '''
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
        '''
        Shows the distribution

        '''
        self.distribution.show()


if __name__ == "__main__":
    from datetime import date, timedelta


    s = DegradationProperty(
        name='sample structure',
        active=True,
        initial_cost=1000,
        initiation_date=date(2000, 1, 1),
        distribution={
            'type': 'gaussian',
            'sigma': timedelta(days=20),
            'mean': timedelta(days=100),
        },
        seed=None
    )

    P = s.probability_of_working(
        start_date=date(2000, 1, 1),
        end_date=date(2000, 1, 1) + timedelta(days=100)
    )
    print(P)

    print(s.is_working(P))

    s.show_distribution()
