from copy import deepcopy


def calculate_market_factor(society, agent, route):

    def market_participants(society, destination): #### active
        #agents_list = society.all_agents(type='active')
        participants = society.all_agents_available(settlement=destination)
        return participants

    participants = market_participants(society, destination=route[1])

    def calculate_source_factor(society, agent):
        result = None
        others = deepcopy(participants)
        others.remove(agent)
        others_source_list = []
        for other in others:
            resource = society.agent_info(other, 'resource')
            source = resource.source()
            others_source_list.append(source)
        source_others = sum(others_source_list)
        agent_resource = society.agent_info(agent, 'resource')
        source_agent = agent_resource.source()
        result = source_others / source_agent
        return result
    
    def calculate_demand_factor(society, agent):
        result = None
        others = deepcopy(participants)
        others.remove(agent)
        others_demand_list = []
        for other in others:
            resource = society.agent_info(other, 'resource')
            demand = resource.demand()
            others_demand_list.append(demand)
        demand_others = sum(others_demand_list)
        agent_resource = society.agent_info(agent, 'resource')
        demand_agent = agent_resource.demand()
        result = demand_others / demand_agent
        return result
    
    source_factor = calculate_source_factor(agent, destination=route[1])
    demand_factor = calculate_demand_factor(agent, destination=route[1])
    buyer_factor = source_factor / demand_factor
    seller_factor = demand_factor / source_factor
    return max(buyer_factor, seller_factor)


if __name__ == "__main__":
    #from piperabm.society.sample import soc_1 as soc
    from piperabm.unit import Date

    #path_graph = soc.env.to_path_graph(start_date=Date(2020, 1, 3), end_date=Date(2020, 1, 5))
    agent = 1
    #path_graph.agent_info(agent, 'settlement')
    route = (0, 1)
    #calculate_market_factor(soc, path_graph, agent, route)