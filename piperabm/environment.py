import matplotlib.pyplot as plt

from piperabm.settlement import Settlement
from piperabm.asset import Asset
from piperabm.graphics.plt.settlement import settlement_to_plt


class Environment:

    def __init__(self, x_lim=[-1,1], y_lim=[-1,1], asset: Asset=None, settlements=[], links=[]):
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.asset = asset
        self.settlements = settlements
        self.links = links
    
    def update_elements(self, start_date, end_date):
        active_settlements = self.filter_active_elements(self.settlements)
        for settlement in active_settlements:
            self.will_work(settlement, start_date, end_date, update=True)

    def filter_active_elements(self, elements):
        result = []
        for element in elements:
            if element.active is True:
                result.append(element)
        return result

    def find_oldest_element(self, elements):
        oldest_date = None
        if len(elements) > 0:
            oldest_date = elements[0].initiation_date
            for element in elements:
                date = element.initiation_date
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
    settlements = []
    links = []

    env = Environment(
        x_lim=[-300, 450],
        y_lim=[-250, 250],
        asset=asset,
        settlements=settlements,
        links=links
    )

