from piperabm.economy.bid import Bid


class Market:

    def __init__(
        self,
        players: list,
        model = None
    ):
        self.model = model  # binding 
        self.players = players
    
    def get(self, index):
        return self.model.get(index)

    def resources(self, index):
        agent = self.get(index)
        return agent.resources
    
    @property
    def exchange_rate(self):
        return self.model.exchange_rate
    
    def agent_demands(self, index):
        resources = self.resources(index)
        return resources.demand
        
    def agent_sources(self, index):
        resources = self.resources(index)
        return resources.source

    def find_biggest_source(self):
        index = None
        resource_name = None
        for index in self.players:
            sources = self.agent_sources(index)
            values = sources.value(self.exchange_rate)
            name = values.biggest
        return index, resource_name
    

if __name__ == "__main__":
    from piperabm.model.samples import model_3
    
    players = model_3.all_alive_agents
    market = Market(players, model_3)
    