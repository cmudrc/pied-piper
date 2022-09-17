from datetime import date
import random


class Structure():
    '''
    Represents a structure that decays over time
    '''
    def __init__(
        self,
        name=None,
        active=True,
        initial_cost=None,
        initiation_date=None,
        coeff=0,
        degree=2,
        seed=None
    ):
        '''
        Create a new structure

        Args:
            name: the structure name, a string
            initial_cost: the structure (initial) built cost, an int or float
            active: whether the infrastructure is active (manually set), True/False value
            initiation_date: the built date, a datetime object
            coeff: used for calculating probability of working currect as a function of time
            degree: used for calculating probability of working currect as a function of time
            seed: used for repeatable random generation
        '''
        self.name = str(name)
        self.active = active
        self.initial_cost = initial_cost

        ''' decay '''
        if isinstance(initiation_date, date):
            self.initiation_date = initiation_date
        else:
            self.initiation_date = None
        self.coeff = coeff
        self.degree = degree

        ''' seed for random '''
        self.seed = seed

    def is_survived(self, date):
        '''
        Checks if the structure survived based weighted random using self.probability_per_time() result.
        It only tells if the instance survived the date or not, won't affect 'self.active'.
        '''
        sequence = [True, False]
        probability = self.probability_per_time(date)
        if self.active is True:  # if is (still) active
            if self.seed is not None:
                random.seed(self.seed)  # if has seed
            result = random.choices(
                sequence, weights=[probability, 1-probability], k=1)
        else:
            result = False
        return result

    def is_working(self, date):
        '''
        Checks if the structure survived based weighted random using self.probability_per_time() result.
        If the instance cannot survive the date, the self.active will be affected
        '''
        sequence = [True, False]
        probability = self.probability_per_time(date)
        if self.active is True:  # if is (still) active
            if self.seed is not None:
                random.seed(self.seed)  # if has seed
            result = random.choices(
                sequence, weights=[probability, 1-probability], k=1)
            if result is False:
                self.active = False  # won't be active anymore
        else:
            result = False
        return result

    def probability_per_time(self, date):
        '''
        Probability of working currect as a function of time
        '''
        start_date = self.initiation_date
        dt = date - start_date
        dt_years = dt.days / 365.25
        degree = self.degree
        coeff = self.coeff
        P = 1 - (coeff * (dt_years ** degree))
        #P = 1 - ((coeff * dt_years) ** degree)
        if P < 0:
            P = 0
        return P

    def __str__(self):
        return self.name


if __name__ == "__main__":
    s = Structure(
        name='sample infrastructure',
        active=True,
        initial_cost=1000,
        initiation_date=date(2000, 1, 1),
        coeff=0.01,
        degree=2,
        seed=208
    )
    print('# Name: ', s)
    for year in range(2000, 2011):
        print('>>> year', year, ':')
        print(' probability of working', ':',
              s.probability_per_time(date(year, 1, 1)))
        print(' is working?', ':', s.is_working(date(year, 1, 1)))
