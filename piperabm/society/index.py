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

    def all_agents(self, type='all'):
        """
        Return a list of all agents' indexes
        """
        result = []
        if type == 'all':
            result = self.index_list
        elif type == 'active':
            for index in self.index_list:
                if self.agent_info(index, 'active') is True:
                    result.append(index)
        return result

    def agent_info(self, agent, property):
        result = None
        index = self.find_agent(agent)
        if index is not None:
            result = self.G.nodes[index][property]
        return result
    
    def set_agent_info(self, agent, property, val):
        index = self.find_agent(agent)
        if index is not None:
            #info = self.agent_info(index, property)
            #info = val
            self.G.nodes[index][property] = val
        else:
            print("ERROR: agent info not updated")
        
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

    def all_max_resource_from(self, agents):
        """
        Calculate all max_resource for a list of agents
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
            max_resource = agent_resource.max_resource
            max_resource = DeltaResource(batch=max_resource)
            result, _ = result + max_resource
        return result

    def all_resource_from(self, agents):
        """
        Calculate all resource for a list of agents
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
            result, _ = result + agent_resource
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
            result, _ = result + demand
        return result
