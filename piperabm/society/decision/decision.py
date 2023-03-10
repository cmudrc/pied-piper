try: from .factors import calculate_market_factor, calculate_fuel_factor
except: from factors import calculate_market_factor, calculate_fuel_factor


class Decision:

    def __init__(self, path_graph, society, agent):
        self.path_graph = path_graph
        self.society = society
        self.agent = agent

    def possible_routes(self):
        """
        A list of possible routes in path graph
        """
        settlement_index = self.society.agent_info(self.agent, 'settlement')
        return self.path_graph.from_node_perspective(settlement_index)
    
    def select_best_route(self):
        """
        Select best possible route based on their scores
        """
        possible_routes = self.possible_routes()
        result = None
        scores = []
        for route in possible_routes:
            score = self.calculate_route_score(route)
            scores.append(score)
        if len(scores) > 0:
            max_index = scores.index(max(scores))
            result = possible_routes[max_index]
        return result
    
    def calculate_route_score(self, route):
        """
        Calculate route score for an agent
        """
        def calculate_score(market_factor, fuel_factor):
            """
            Calculate the score based on the factors
            """
            return market_factor / fuel_factor

        market_factor = calculate_market_factor(
            society=self.society,
            agent=self.agent,
            route=route
        )
        fuel_factor = calculate_fuel_factor(
            society=self.society,
            path_graph=self.path_graph,
            agent=self.agent,
            route=route
        )
        return calculate_score(
            market_factor,
            fuel_factor
        )


if __name__ == "__main__":
    from piperabm.society.sample import soc_1 as soc
    from piperabm.unit import Date, DT
    
    agents = soc.all_agents()
    agent = agents[1]
    start_date = Date.today() + DT(days=1)
    end_date = start_date + DT(days=1)
    path_graph = soc.env.to_path_graph(start_date, end_date)
    #path_graph.show()
    decision = Decision(path_graph, soc, agent)
    possible_routes = decision.possible_routes()
    print(possible_routes)
    route = possible_routes[0]
    score = decision.calculate_route_score(route)
    print(score)
    best_route = decision.select_best_route()
    print(best_route)