class Transaction:

    def __init__(self, agent, wallet, resource):
        self.agent = agent
        self.wallet = wallet
        self.resource = resource
        self.score = None

    def demand(self):
        return self.resource.demand()

    def source(self):
        return self.resource.source()