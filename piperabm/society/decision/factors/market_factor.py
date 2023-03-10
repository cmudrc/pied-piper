from copy import deepcopy

from piperabm.resource import resource_sum


def calculate_market_factor(society, agent, route):

    def trade_participants(society, target): #### active
        #agents_list = society.all_agents(type='active')
        participants = society.all_agents_available(settlement=target)
        return participants

    participants = trade_participants(society, target=route[1])
    #print(participants)##########

    def calculate_source_factor(society, agent):
        result = None
        others = deepcopy(participants)
        if agent in others: others.remove(agent)
        others_source_list = []
        for other in others:
            resource = society.agent_info(other, 'resource')
            source = resource.source()
            others_source_list.append(source)
        source_others = resource_sum(others_source_list)
        agent_resource = society.agent_info(agent, 'resource')
        source_agent = agent_resource.source()
        result = source_others / source_agent
        return result
    
    def calculate_demand_factor(society, agent):
        result = None
        others = deepcopy(participants)
        if agent in others: others.remove(agent)
        others_demand_list = []
        for other in others:
            resource = society.agent_info(other, 'resource')
            demand = resource.demand()
            others_demand_list.append(demand)
        demand_others = resource_sum(others_demand_list)
        agent_resource = society.agent_info(agent, 'resource')
        demand_agent = agent_resource.demand()
        result = demand_others / demand_agent
        return result
    
    source_factor = calculate_source_factor(society, agent)
    demand_factor = calculate_demand_factor(society, agent)
    buyer_factor = source_factor / demand_factor
    seller_factor = demand_factor / source_factor
    buyer_factor_max = buyer_factor(buyer_factor.max())
    seller_factor_max = seller_factor(seller_factor.max())
    return max(buyer_factor_max, seller_factor_max)


if __name__ == "__main__":
    from piperabm.society.sample import soc_1 as soc
    from piperabm.unit import Date, DT

    agents = soc.all_agents()
    agent = agents[0]
    #start_date = Date.today() + DT(days=1)
    #end_date = start_date + DT(days=1)
    #path_graph = soc.env.to_path_graph(start_date, end_date)
    #path_graph.show()
    route = (0, 1)
    factor = calculate_market_factor(
        society=soc,
        agent=agent,
        route=route
    )
    print(factor)