class Decision:

    def possible_routes(self, agent, start_date, end_date):
        """
        A list of possible routes in path graph
        """
        settlement_index = self.agent_info(agent, 'settlement')
        path = self.env.to_path(start_date, end_date)
        return list(path.from_node_perspective(settlement_index))

    def select_best_route(self, agent, start_date, end_date):
        """
        Select best possible route based on their scores
        """
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
        def score(resource_factor, time_factor, fuel_factor):
            """
            Calculate the score based on the factors
            """
            return resource_factor / (time_factor * fuel_factor)

        def time_factor(agent, path):
            """
            Calculate duration of the trip
            """
            required_time_list = []
            for link in path:
                adjusted_length = path.env.adjusted_length(*link)
                transportation = self.agent_info(agent, 'transportation')
                required_time = transportation.how_long(adjusted_length).total_seconds()
                required_time_list.append(required_time)
            return sum(required_time_list)

        def resource_factor(agent, destination):
            """
            Ratio of all resource available in destination to agent's current resource
            """
            resource = self.agent_info(agent, 'resource')
            current_resource = resource.current_resource
            agents = self.all_agents_available(destination)
            all_resource = self.all_resource_from(agents)
            ratio_dict = all_resource / current_resource
            return min(list(ratio_dict.values()))

        def fuel_factor(agent, path):
            """
            Ratio of required fuel until destination to agent's current resource
            """
            fuel_factor_list = []
            resource = self.agent_info(agent, 'resource')
            current_resource = resource.current_resource
            transportation = self.agent_info(agent, 'transportation')
            for link in path:
                adjusted_length = path.env.adjusted_length(*link)
                required_fuel = transportation.how_much_fuel(adjusted_length)
                fuel_factor_dict = required_fuel / current_resource
                fuel_factor = max(list(fuel_factor_dict.values()))
                fuel_factor_list.append(fuel_factor)
            return sum(fuel_factor_list)

        path_graph = self.env.to_path(start_date, end_date)
        path = path_graph.route_info(*route, 'path')
        tf = time_factor(agent, path)
        rf = resource_factor(agent, route)
        ff = fuel_factor(agent, path)
        return score(resource_factor=rf, time_factor=tf, fuel_factor=ff)
