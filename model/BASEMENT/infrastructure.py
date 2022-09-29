import json
from datetime import date

from core.structure import Structure


class Infrastructure(Structure):
    '''
    Represents infrastructures, such as roads and pipelines
    '''

    def __init__(
        self,
        start=None,
        end=None,
        resources=None,
        **kwargs
    ):
        '''
        Create a new infrastructure

        Args:
            name: route name
            start: the starting point name
            end: the ending point name
            resources: a dictionary of {"resource name": max_discharge} pairs
            self.current_discharge: a dictionary like above, only with current_discharge value
            **kwargs: the variables for initializing the Structure class
        '''
        super().__init__(**kwargs)
        self.start = start
        self.end = end
        self.resources = resources
        self.current_discharge = None

    def to_json(self):
        ''' converts all the information within the instance into json '''
        result = dict()
        result['name'] = self.name
        result['type'] = self.type
        result['start'] = self.start
        result['end'] = self.end
        result['two_sided'] = self.two_sided
        result['resources'] = self.resources
        result['cost'] = self.cost
        result['active'] = self.active
        result['project_start_date'] = {
            'year': self.project_start_date.year,
            'month': self.project_start_date.month,
            'day': self.project_start_date.day
        }
        result['coeff'] = self.coeff
        result['degree'] = self.degree
        result['seed'] = self.seed
        return json.dumps(result)

    def from_json(self, txt):
        ''' loads all the information from json into instance '''
        info = json.loads(txt)
        self.name = info['name']
        self.type = info['type']
        self.start = info['start']
        self.end = info['end']
        self.two_sided = info['two_sided']
        self.resources = info['resources']
        self.cost = info['cost']
        self.active = info['active']
        self.project_start_date = date(
            info['project_start_date']['year'],
            info['project_start_date']['month'],
            info['project_start_date']['day'],
        )
        self.coeff = info['coeff']
        self.degree = info['degree']
        self.seed = info['seed']


if __name__ == "__main__":
    from datetime import date

    i = Infrastructure(
        name='sample road',
        start='city_1',
        end='city_2',
        resources={
            'water': 5,
        },
        initial_cost=1000,
        initiation_date=date(2000, 1, 1),
        coeff=0.01,
        degree=2,
        seed=208
    )
    print('# Name: ', i)
    for year in range(2000, 2011):
        print('>>> year', year, ':')
        print(' probability of working', ':',
              i.probability_per_time(date(year, 1, 1)))
        print(' is working?', ':', i.is_working(date(year, 1, 1)))

    #j_1 = i.to_json()
    #print(j_1)
    #k = Infrastructure()
    #k.from_json(j)
    #j_2 = k.to_json()
