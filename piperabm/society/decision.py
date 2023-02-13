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
            score = self.calculate_route_score(agent, route, start_date, end_date)
            scores.append(score)
        max_index = scores.index(max(scores))
        return possible_routes[max_index]

    def calculate_route_score(self, agent, route, start_date, end_date):
        """
        Calculate route score for an agent
        """
        path_graph = self.env.to_path(start_date, end_date)
        data = path_graph.G[route[0]][route[1]]
        path = data['path']
        adjusted_length_list = []
        resource_factor_list = []
        required_time_list = []
        current_resource = agent.resource.current_resource
        for link in path:
            data = self.env.G[link[0]][link[1]]
            adjusted_length = self.env.adjusted_length(*link)
            adjusted_length_list.append(adjusted_length) # length
            required_time = agent.transportation.how_long(adjusted_length).total_seconds()
            required_time_list.append(required_time) # time
            required_resource = agent.transportation.how_much_fuel(adjusted_length)
            resource_factor_dict = required_resource / current_resource
            resource_factor = max(list(resource_factor_dict.values()))
            resource_factor_list.append(resource_factor) # resource
        time_factor = sum(required_time_list)
        resource_factor = sum(resource_factor_list)
        score = 1 / (time_factor * resource_factor)
        return score
