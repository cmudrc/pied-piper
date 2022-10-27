from asset import Produce, Storage, Resource, Use, Asset


class Environment:

    def __init__(self, x_lim, y_lim, asset):
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.asset = asset
    
    def update(self, start_date, end_date):
        pass


if __name__ == "__main__":
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

    env = Environment(
        x_lim=[-500, 500],
        y_lim=[-300, 300],
        asset=asset
    )

