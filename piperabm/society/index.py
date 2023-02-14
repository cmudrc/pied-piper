from piperabm.resource import DeltaResource


class Index:
    
    def __init__(self):
        self.index_list = []

    def find_next_index(self):
        """
        Check self.index_list (indexes) and suggest a new index
        """
        index_list = self.index_list
        if len(index_list) > 0:
            max_index = max(index_list)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

    def agent_info(self, agent, property):
        index = self.find_agent(agent)
        return self.G.nodes[index][property]
        
    def all_agents_from(self, settlement):
        """
        Create a list of agent indexes that are from *settlement*
        """
        result = []
        for index in self.index_list:
            agent_settlement = self.agent_info(index, 'settlement')
            if agent_settlement == settlement:
                result.append(index)
        return result

    def all_resource_from(self, settlement):
        result = DeltaResource(
            {
                'food': 0,
                'water': 0,
                'energy': 0,
            }
        )
        agents_from_settlement = self.all_agents_from(settlement)
        for agent in agents_from_settlement:
            agent_resource = self.agent_info(agent, 'resource')
            agent_resource = agent_resource.to_delta_resource()
            result = result + agent_resource
        return result

    def all_demand_from(self, settlement):
        result = DeltaResource(
            {
                'food': 0,
                'water': 0,
                'energy': 0,
            }
        )
        agents_from_settlement = self.all_agents_from(settlement)
        for agent in agents_from_settlement:
            agent_resource = self.agent_info(agent, 'resource')
            demand = agent_resource.demand()
            result = result + demand
