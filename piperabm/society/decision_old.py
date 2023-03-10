class Decision:

    def possible_routes(self, agent, start_date, end_date):
        """
        A list of possible routes in path graph
        """
        settlement_index = self.agent_info(agent, 'settlement')
        path_graph = self.env.to_path_graph(start_date, end_date)
        return path_graph.from_node_perspective(settlement_index)
    
    def select_best_route(self, agent, start_date, end_date):
        """
        Select best possible route based on their scores
        """
        possible_routes = self.possible_routes(agent, start_date, end_date)
        result = None
        scores = []
        for route in possible_routes:
            score = self.calculate_route_score(agent, route, start_date, end_date)
            scores.append(score)
        if len(scores) > 0:
            max_index = scores.index(max(scores))
            result = possible_routes[max_index]
        return result
    
    def calculate_route_score(self, agent, route, start_date, end_date):
        """
        Calculate route score for an agent
        """
        def calculate_score(resource_factor, fuel_factor):
            """
            Calculate the score based on the factors
            """
            return resource_factor / fuel_factor

        '''
        def calculate_time_factor(agent, path):
            """
            Calculate duration of the trip
            """
            required_time_list = []
            for i, _ in enumerate(path.path):
                if i > 0:
                    _from = path.path[i-1]
                    _to = path.path[i]
                    adjusted_length = self.env.adjusted_length(_from, _to)
                    transportation = self.agent_info(agent, 'transportation')
                    required_time = transportation.how_long(adjusted_length).total_seconds()
                    required_time_list.append(required_time)
            return sum(required_time_list)
        '''

        def calculate_market_factor(agent, destination):

            def calculate_source_factor(agent, destination):
                result = None
                source_others = None
                agent_resource = self.agent_info(agent, 'resource')
                source_agent = agent_resource.source()
                result = source_others / source_agent
                return result
            
            def calculate_demand_factor(agent, destination):
                result = None
                others = self.all_agents()
                others.remove(agent)
                others_demand_list = []
                for other in others:
                    resource = self.agent_info(other, 'resource')
                    demand = resource.demand()
                    others_demand_list.append(demand)
                demand_others = sum(others_demand_list)
                agent_resource = self.agent_info(agent, 'resource')
                demand_agent = agent_resource.demand()
                result = demand_others / demand_agent
                return result


            source_factor = calculate_source_factor(agent, destination)
            demand_factor = calculate_demand_factor(agent, destination)
            buyer_factor = source_factor / demand_factor
            seller_factor = demand_factor / source_factor
            return max(buyer_factor, seller_factor)

        '''
        def resource_factor(agent, destination):
            """
            Ratio of all resource available in destination to agent's current resource
            """
            resource = self.agent_info(agent, 'resource')
            agents = self.all_agents_available(destination)
            all_resource = self.all_resource_from(agents)
            resource_delta = all_resource / resource
            result_list = list(resource_delta.batch.values())
            if len(result_list) > 0:
                result = max(result_list)
            else:
                result = 0
            return result
        '''

        def calculate_fuel_factor(agent, path):
            """
            Ratio of required fuel until destination to agent's current resource
            """
            fuel_factor_list = []
            resource = self.agent_info(agent, 'resource')
            transportation = self.agent_info(agent, 'transportation')
            for i, _ in enumerate(path.path):
                if i > 0:
                    _from = path.path[i-1]
                    _to = path.path[i]
                    adjusted_length = self.env.adjusted_length(_from, _to)
                    required_fuel = transportation.how_much_fuel(adjusted_length)
                    fuel_factor_delta = required_fuel / resource
                    fuel_factor = max(list(fuel_factor_delta.batch.values()))
                    fuel_factor_list.append(fuel_factor)
            return sum(fuel_factor_list)

        path_graph = self.env.to_path_graph(start_date, end_date)
        path = path_graph.edge_info(*route, 'path')
        #tf = time_factor(agent, path)
        rf = calculate_market_factor(agent, route[1])
        ff = calculate_fuel_factor(agent, path)
        return calculate_score(resource_factor=rf, fuel_factor=ff)


class Decision:

    def possible_routes(self, agent, start_date, end_date):
        """
        A list of possible routes in path graph
        """
        settlement_index = self.agent_info(agent, 'settlement')
        path_graph = self.env.to_path_graph(start_date, end_date)
        #path_graph.show()
        #print(settlement_index)
        result = path_graph.from_node_perspective(settlement_index)
        #print(result)
        return result

    def select_best_route(self, agent, start_date, end_date):
        """
        Select best possible route based on their scores
        """
        possible_routes = self.possible_routes(agent, start_date, end_date)
        result = None
        scores = []
        for route in possible_routes:
            score = self.calculate_route_score(agent, route, start_date, end_date)
            scores.append(score)
        if len(scores) > 0:
            max_index = scores.index(max(scores))
            result = possible_routes[max_index]
        return result

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
            for i, _ in enumerate(path.path):
                if i > 0:
                    _from = path.path[i-1]
                    _to = path.path[i]
                    adjusted_length = self.env.adjusted_length(_from, _to)
                    transportation = self.agent_info(agent, 'transportation')
                    required_time = transportation.how_long(adjusted_length).total_seconds()
                    required_time_list.append(required_time)
            return sum(required_time_list)

        def resource_factor(agent, destination):
            """
            Ratio of all resource available in destination to agent's current resource
            """
            resource = self.agent_info(agent, 'resource')
            agents = self.all_agents_available(destination)
            all_resource = self.all_resource_from(agents)
            resource_delta = all_resource / resource
            result_list = list(resource_delta.batch.values())
            if len(result_list) > 0:
                result = max(result_list)
            else:
                result = 0
            return result

        def fuel_factor(agent, path):
            """
            Ratio of required fuel until destination to agent's current resource
            """
            fuel_factor_list = []
            resource = self.agent_info(agent, 'resource')
            transportation = self.agent_info(agent, 'transportation')
            for i, _ in enumerate(path.path):
                if i > 0:
                    _from = path.path[i-1]
                    _to = path.path[i]
                    adjusted_length = self.env.adjusted_length(_from, _to)
                    required_fuel = transportation.how_much_fuel(adjusted_length)
                    fuel_factor_delta = required_fuel / resource
                    fuel_factor = max(list(fuel_factor_delta.batch.values()))
                    fuel_factor_list.append(fuel_factor)
            return sum(fuel_factor_list)

        path_graph = self.env.to_path_graph(start_date, end_date)
        path = path_graph.edge_info(*route, 'path')
        tf = time_factor(agent, path)
        rf = resource_factor(agent, route[1])
        ff = fuel_factor(agent, path)
        return score(resource_factor=rf, time_factor=tf, fuel_factor=ff)
