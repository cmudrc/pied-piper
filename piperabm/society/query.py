from piperabm.resource import Resource, resource_sum


class Query:
    """
    Contains methods for Society class
    Create a wrap-up for accessing data
    """

    def all_agents(self, type='all'):
        """
        Return a list of all agents' indexes
        """
        def check_active(agent_index):
            agents = self.get_agents([agent_index])
            agent = agents[0]
            agent_origin_index = agent.origin_node
            is_active = self.env.link_graph.node_info(agent_origin_index, 'currently_active')
            return is_active
        
        def check_alive(agent_index):
            agents = self.get_agents([agent_index])
            agent = agents[0]
            return agent.alive

        result = []
        if type == 'all':
            result = self.index_list
        elif type == 'alive':
            for index in self.index_list:
                if check_alive(index):
                    result.append(index)
        elif type == 'active':
            for index in self.index_list:
                if check_active(index):
                    result.append(index)
        elif type == 'active&alive':
            for index in self.index_list:
                if check_active(index) \
                    and check_alive(index):
                    result.append(index)
        return result
    
    def agent_info(self, agent, property):
        result = None
        agent_index = self.find_agent(agent)
        if agent_index is not None:
            result = getattr(agent_index, property)
        return result
    
    def set_agent_info(self, agent, property, val):
        agent = self.find_agent(agent)
        if agent is not None:
            setattr(agent, property, val)
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