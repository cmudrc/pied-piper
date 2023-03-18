from piperabm.resource import Resource, resource_sum


class Query:
    """
    Contains methods for Society class
    Create a wrap-up for accessing graph data
    """

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
            agent = self.G.nodes[index]['agent']
            result = getattr(agent, property)
        return result
    
    def set_agent_info(self, agent, property, val):
        index = self.find_agent(agent)
        if index is not None:
            #info = self.agent_info(index, property)
            #info = val
            agent = self.G.nodes[index]['agent']
            setattr(agent, property, val)
            #self.G.nodes[index][property] = val
        else:
            print("ERROR: agent info not updated")
        
    def all_agents_from(self, settlement, agents_list=None):
        """
        Create a list of agent indexes that are from *settlement*
        """
        result = []
        if agents_list is None:
            index_list = self.index_list
        else:
            index_list = agents_list
        for index in index_list:
            agent_settlement = self.agent_info(index, 'origin_node')
            if agent_settlement == settlement:
                result.append(index)
        return result

    def all_agents_in(self, settlement):
        """
        Create a list of agent indexes showing all agents that are inside the *settlement*
        """
        result = []
        for index in self.index_list:
            current_settlement = self.agent_info(index, 'current_node')
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
        result = []
        for agent in agents:
            agent_resource = self.agent_info(agent, 'resource')
            max_resource = agent_resource.max_resource
            max_resource = Resource(max_resource)
            result.append(max_resource)
        return resource_sum(result)

    def all_resource_from(self, agents):
        """
        Calculate all resource for a list of agents
        """
        if isinstance(agents, int):
            agents = [agents]
        result = []
        for agent in agents:
            agent_resource = self.agent_info(agent, 'resource')
            result.append(agent_resource)
        return resource_sum(result)

    def all_demand_from(self, agents):
        """
        Calculate all demand from list of agents
        """
        if isinstance(agents, int):
            agents = [agents]
        result = []
        for agent in agents:
            agent_resource = self.agent_info(agent, 'resource')
            demand = agent_resource.demand()
            result.append(demand)
        return resource_sum(result)