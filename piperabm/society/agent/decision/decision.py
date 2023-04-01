from piperabm.actions import Trade, Move, Walk

try: from .factors import calculate_fuel_factor, MarketFactor
except: from factors import calculate_fuel_factor, MarketFactor


class Decision:

    def observe(self, society):
        self.society = society
        self.path_graph = self.society.env.path_graph
        self.start_date = self.path_graph.start_date
        self.end_date = self.path_graph.end_date

    def possible_routes(self):
        """
        A list of possible routes in path graph
        """
        return self.path_graph.from_node_perspective(self.current_node)
    
    def select_best_route(self):
        """
        Select best possible route based on their scores
        """

        def max_score(scores):
            result = None
            refined_scores = []
            for score in scores:
                if score is not None:
                    refined_scores.append(score)
            if len(refined_scores) > 0:
                result = max(refined_scores)
            return result

        possible_routes = self.possible_routes()
        result = None
        scores = []
        for route in possible_routes:
            score = self.calculate_route_score(route)
            scores.append(score)
        if len(scores) > 0:
            max_index = scores.index(max_score(scores))
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
            result = None
            if market_factor is not None and \
            fuel_factor is not None and \
            fuel_factor != 0:
                result = market_factor / fuel_factor
            return result

        market_factor_calculator = MarketFactor(
            society=self.society,
            agent_index=self.index,
            route=route
        )
        market_factor = market_factor_calculator.calculate()
        fuel_factor = calculate_fuel_factor(
            society=self.society,
            path_graph=self.path_graph,
            agent_index=self.index,
            route=route
        )
        return calculate_score(
            market_factor,
            fuel_factor
        )

    def decide_action(self):
        route = self.select_best_route()
        if route is not None:
            path = self.path_graph.edge_info(*route, 'path')
            move = Move(
                start_date=self.start_date,
                path=path,
                transportation=Walk()
            )
            self.queue.add(move)
            trade = Trade(start_date=self.start_date)
            self.queue.add(trade)
            ''' log '''
            #msg = self.log.message__agent_decided(
            #    route=route,
            #    agent_index=index,
            #    agent_name=self.agent_info(index, 'name'),
            #    agent_pos=self.agent_info(index, 'pos')
            #)
            #print(msg)


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