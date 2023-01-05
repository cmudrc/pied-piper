import matplotlib.pyplot as plt

from piperabm.settlement import Settlement
from piperabm.link import Cross, Track
from piperabm.asset import Asset
from piperabm.tools import find_element, euclidean_distance
from piperabm.graphics.plt.settlement import settlement_to_plt


class Environment:

    def __init__(self, x_lim=[-1,1], y_lim=[-1,1], asset: Asset=None, settlements=[], links=[]):
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.asset = asset
        self.settlements = settlements
        self.links = links
        self.crosses = []

    def add_settlement(self, settlement:Settlement):
        """
        Add new settlement to the environment
        """
        self.settlements.append(settlement)

    def add_link(self, start, end, length=None, difficulty=1):
        """
        Add new link to the environment
        """
        start_name = self.find_node(start)
        end_name = self.find_node(end)
        link = Track(start_name, end_name)
        """ update *length* """
        ## find start_pos
        start_element = find_element(start_name, self.settlements)
        if start_element is None:
            start_element = find_element(start_name, self.crosses)
        start_pos = start_element.boundery.center
        ## find end_pos
        end_element = find_element(end_name, self.settlements)
        if end_element is None:
            end_element = find_element(end_name, self.crosses)
        end_pos = end_element.boundery.center
        ## update #length*
        distance = euclidean_distance(*start_pos, *end_pos)
        if length is None:
            length = distance
        else:
            if length < distance:
                raise ValueError
        link.length = length
        link.difficulty = difficulty
        self.links.append(link)
        
    def find_node(self, point):
        """
        Find the settlement/cross instance that contains *point* within
        if no settlement/cross was found, a new cross instance would be generated
        """
        result = None
        # input based on settlement/cross name
        if isinstance(point, str):
            for settlement in self.settlements:
                if settlement.name == point:
                    result = settlement
            for cross in self.crosses:
                if cross.name == point:
                    result = cross
        # input based on position
        elif isinstance(point, list) and len(point) == 2:
            for settlement in self.settlements:
                if settlement.is_in(point):
                    result = settlement
            for cross in self.crosses:
                if cross.is_in(point):
                    result = cross
            # if node not found, create it:
            if result is None:
                result = Cross(pos=point, all_cross=self.crosses)
                self.crosses.append(result)
        return result.name

    def update_elements(self, start_date, end_date):
        active_settlements = self.filter_active_elements(self.settlements)
        for settlement in active_settlements:
            result = self.will_work(settlement, start_date, end_date, update=True)
            #print(result)

    def filter_active_elements(self, elements):
        result = []
        for element in elements:
            if element.active is True:
                result.append(element)
        return result

    def find_oldest_element(self, elements):
        """
        Find the oldest initiation_date of the elements
        """
        oldest_date = None
        if len(elements) > 0:  
            for element in elements:
                date = element.initiation_date
                if date is not None:
                    if oldest_date is None: oldest_date = date
                    else:
                        if date < oldest_date:
                            oldest_date = date
        return oldest_date

    def will_work(self, element, start_date, end_date, update:bool=True):
        probability = element.probability_of_working(start_date, end_date)
        result = element.is_working(probability)
        if update:
            element.active = result
        return result

    def to_dict(self) -> dict:
        settlements_list = []
        for settlement in self.settlements:
            settlements_list.append(settlement.to_dict())
        dictionary = {
            'x_lim': self.x_lim,
            'y_lim': self.y_lim,
            'asset': self.asset.to_dict(),
            'settlements': settlements_list
        }
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        self.x_lim = d['center']
        self.y_lim = d['radius']
        self.asset = Asset().from_dict(d['asset'])
        settlements_list = d['settlements']
        self.settlements = []
        for settlement_dict in settlements_list:
            s = Settlement()
            s.from_dict(settlement_dict)
            self.settlements.append(s)

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        for settlement in self.settlements:
            settlement_to_plt(settlement.to_dict(), ax)

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis('equal')
        plt.xlim(self.x_lim)
        plt.ylim(self.y_lim)
        self.to_plt(ax)
        plt.show()


if __name__ == "__main__":
    from piperabm.asset import Produce, Storage, Resource, Use, Asset
    
    resources = [
        Resource(
            name='water',
            produce=Produce(rate=0.1),
            storage=Storage(current_amount=5, max_amount=10),
        ),
        Resource(
            name='food',
            produce=Produce(rate=0.1),
            storage=Storage(current_amount=5, max_amount=10),
        ),
        Resource(
            name='energy',
            produce=Produce(rate=0),
            storage=Storage(current_amount=100, max_amount=None),
        ),
    ]

    asset = Asset(resources)
    settlements = [
        Settlement(
            name='s_1',
            pos=[0,0],
            boundery=None
        ),
    ]
    links = []

    env = Environment(
        x_lim=[-300, 450],
        y_lim=[-250, 250],
        asset=asset,
        settlements=settlements,
        links=links
    )

    env.add_link(start=[0,0], end=[20,20], length=30)
    env.add_link(start=[20.5,20], end=[30,30])

    for cross in env.crosses:
        print(cross.boundery.center)