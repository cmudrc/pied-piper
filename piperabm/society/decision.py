class Decision:

    def possible_routes(self, agent, start_date, end_date):
        index = self.find_agent(agent)
        node = self.G.nodes[index]
        settlement_index = node['settlement']
        path = self.env.to_path(start_date, end_date)
        return path.from_node_perspective(settlement_index)

    def select_best_route(self, agent, start_date, end_date):
        possible_routes = self.possible_routes(agent, start_date, end_date)
        scores = []
        for route in possible_routes:
            score = self.score(agent, route)
            scores.append(score)
        ###

    def calculate_score(self, agent, route):
        pass