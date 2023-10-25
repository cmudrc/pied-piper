class Bid:

    def __init__(
        self,
        resource_name,
        exchange_rate
    ):
        self.market = None  # binding
        self.resource_name = resource_name
        self.exchange_rate = exchange_rate
