from copy import deepcopy

from piperabm.resource import resource_sum


class MarketFactor:

    def __init__(self, agent, route):
        self.society = agent.society
        self.agent_index = agent.index
        self.agent = agent #####
        self.route = route
        self.participants = self.trade_participants(target=route[1])

    def trade_participants(self, target): #### active
        #agents_list = society.all_agents(type='active')
        return self.society.all_agents_available(settlement=target)
    
    def calculate_source_factor(self):
        result = None
        others = deepcopy(self.participants)
        society = self.society
        agent = self.agent_index
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
    
    def calculate_demand_factor(self):
        result = None
        others = deepcopy(self.participants)
        society = self.society
        agent = self.agent_index
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

    def calculate(self):
        source_factor = self.calculate_source_factor()
        demand_factor = self.calculate_demand_factor()
        buyer_factor = source_factor / demand_factor
        seller_factor = demand_factor / source_factor
        #print(self.agent_index)
        #print(buyer_factor, seller_factor)
        #print(buyer_factor.max(), seller_factor.max())
        buyer_factor_max = buyer_factor(buyer_factor.max())
        seller_factor_max = seller_factor(seller_factor.max())
        #print(buyer_factor_max, seller_factor_max)

        def custom_max(val_1, val_2):
            result = None
            if val_1 is not None:
                if val_2 is not None:
                    result = max(val_1, val_2)
            return result
        
        return custom_max(buyer_factor_max, seller_factor_max)


if __name__ == "__main__":
    from piperabm.society.sample import sample_society_0
    from piperabm.unit import Date

    society = deepcopy(sample_society_0)
    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    society.env.update_elements(start_date, end_date)
    agent = society.find_agent(agent_info=0)
    #print(agent)
    agent.observe(society)
    agent_route = (0, 1)
    market_factor_calculator = MarketFactor(
        agent=agent,
        route=agent_route
    )
    market_factor = market_factor_calculator.calculate()
    print(market_factor)
