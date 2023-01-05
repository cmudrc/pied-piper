import numpy as np

try:
    from .distributions import Gaussian, DiracDelta, Eternal
except:
    from distributions import Gaussian, DiracDelta, Eternal
    

class DegradationProperty:
    """
    Represents degradation property of an object that degrades over time.
    """

    def __init__(
        self,
        active=True,
        coeff=1,
        initial_cost=None,
        initiation_date=None,
        distribution=None,
        seed=None
    ):
        """
        Args:
            active: is the object still active?
            coeff: coefficient for *Q* (probability of not working), useful for link class instances
            initial_cost: cost of building the structure
            initiation_date: date in which it was built
            distribution: a dictionary containing information about the districbution function of life expectency
            seed: for repeatable results
        """

        self.active = active
        self.coeff = coeff
        self.initial_cost = initial_cost
        self.renovation_effect = None
        self.initiation_date = initiation_date
        self.add_distribution(distribution)
        self.seed = seed

    def degradation_to_dict(self) -> dict:
        dictionary = {
            'active': self.active,
            'initial_cost': self.initial_cost,
            'initiation_date': self.initiation_date,
            'distribution': self.distribution.to_dict(),
            'seed': self.seed
        }
        return dictionary

    def degradation_from_dict(self, dictionary: dict):
        d = dictionary
        self.active = d['active']
        self.initial_cost = d['initial_cost']
        self.initiation_date = d['initiation_date']
        self.add_distribution(d['distribution'])
        self.seed = d['seed']

    def _add_distribution_from_dict(self, distribution_dict: dict):
        distribution = distribution_dict
        if distribution['type'] == 'gaussian':
            self.distribution = Gaussian(
                mean=distribution['mean'],
                sigma=distribution['sigma']
            )
        elif distribution['type'] == 'dirac delta':
            self.distribution = DiracDelta(
                main=distribution['main']
            )
        elif distribution['type'] == 'eternal':
            self.distribution = Eternal()
        else:
            self.distribution = Eternal()

    def add_distribution(self, distribution):
        if isinstance(distribution, dict):
            self._add_distribution_from_dict(distribution_dict=distribution)
        elif isinstance(distribution, 
            (
                Gaussian,
                DiracDelta,
                Eternal
            )
        ):
            self.distribution = distribution
        elif distribution is None:
            self.distribution = Eternal()
    
    '''
    def renovation_effect_calc(self, renovation_cost, current_date):
        delta_t = (current_date - self.initiation_date)
        return delta_t * (renovation_cost / self.initial_cost)
    '''
    
    def probability_of_working(self, start_date, end_date):
        """
        Probability of remaining active during the desired duration of time.
        
        Args:
            start_date: start of duration of time, datetime object
            end_date: end of duration of time, datetime object
        
        """
        t1 = start_date
        t2 = end_date
        if isinstance(self.distribution, Eternal):
            t0 = t1
        else:
            t0 = self.initiation_date

        Q = self.distribution.probability(
            time_start=(t1-t0).total_seconds(),
            time_end=(t2-t0).total_seconds()
        )
        Q *= self.coeff
        if Q > 1: Q = 1
        P = 1 - Q
        return P

    def is_working(self, probability):
        """
        Check if the structure survived based on weighted random and returns the result (True/False).
        
        Args:
            probability: probability of working (or remaining alive) at each step
        
        """
        result = False
        sequence = [True, False]  # set of possible outcomes
        weights = [probability, 1-probability]
        if self.active is True:  # if is (still) active
            #if self.seed is not None: np.random.seed(self.seed)  # if has seed
            index = np.random.choice(
                2, # np.arange(1)
                1, # return one element
                p=weights
            )
            result = sequence[int(index)]
        return result

    def is_active(self, start_date, end_date, update=False):
        """
        Check if the element is going to survive the desired duration of time or not.
        Updates the self.active as result.

        Args:
            start_date: start of duration of time, datetime object
            end_date: end of duration of time, datetime object
        
        Returns:
            self.active (True/False)
        """
        probability = self.probability_of_working(start_date, end_date)
        active = self.is_working(probability)
        if update is True:
            self.active = active
        return active

    def show_distribution(self):
        """
        Shows the distribution

        """
        self.distribution.show()


if __name__ == "__main__":
    from piperabm.unit import Unit, Date


    s = DegradationProperty(
        initiation_date=Date(2000, 1, 1),
        distribution={
            'type': 'gaussian',
            'sigma': Unit(20,'day').to('second').val,
            'mean': Unit(100,'day').to('second').val,
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
        initiation_date=Date(2000, 1, 1),
        distribution={
            'type': 'dirac delta',
            'main': Unit(10,'day').to('second').val,
        },
        seed=202
    )

    #P = d.probability_of_working(
    #    start_date=Unit(0, 'day')+date(2000, 1, 1),
    #    end_date=Unit(15, 'day')+date(2000, 1, 1)
    #)
    activeness = d.is_active(
        start_date=Unit(0, 'day')+Date(2000, 1, 1),
        end_date=Unit(5, 'day')+Date(2000, 1, 1)
    )
    print(activeness)

    #print(s.is_working(P))

    #s.show_distribution()