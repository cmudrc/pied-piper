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

    def all_agents(self):
        """
        Return a list of all agents' indexes
        """
        return self.index_list

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

    def all_agents_in(self, settlement):
        """
        Create a list of agent indexes showing all agents that are inside the *settlement*
        """
        result = []
        for index in self.index_list:
            current_settlement = self.agent_info(index, 'current_settlement')
            if current_settlement == settlement:
                result.append(index)
        return result

    def all_agents_available(self, settlement):
        """
        All agents available for market in *settlement*
        """
        result = []
        all_agents_in = self.all_agents_in(settlement)
        all_agents_from = self.all_agents_from(settlement)
        for index in all_agents_in:
            if index not in result:
                result.append(index)
        for index in all_agents_from:
            if index not in result:
                result.append(index)
        return result

    def all_resource_from(self, agents):
        """
        Calculate all resource from list of agents
        """
        if isinstance(agents, int):
            agents = [agents]
        result = DeltaResource(
            {
                'food': 0,
                'water': 0,
                'energy': 0,
            }
        )
        for agent in agents:
            agent_resource = self.agent_info(agent, 'resource')
            agent_resource = agent_resource.to_delta_resource()
            result = result + agent_resource
        return result

    def all_demand_from(self, agents):
        """
        Calculate all demand from list of agents
        """
        if isinstance(agents, int):
            agents = [agents]
        result = DeltaResource(
            {
                'food': 0,
                'water': 0,
                'energy': 0,
            }
        )
        for agent in agents:
            agent_resource = self.agent_info(agent, 'resource')
            demand = agent_resource.demand()
            result = result + demand
        return result
