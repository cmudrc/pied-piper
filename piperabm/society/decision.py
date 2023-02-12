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
            score = self.calculate_score(agent, route)
            scores.append(score)
        max_index = scores.index(max(scores))
        return possible_routes[max_index]

    def calculate_route_score(self, agent, route, start_date, end_date):
        path_graph = self.env.to_path(start_date, end_date)
        data = path_graph.G[route[0]][route[1]]
        path = data['path']
        adjusted_length_list = []
        required_resource_list = []
        current_resource_list = []
        for link in path:
            data = self.env.G[link[0]][link[1]]
            adjusted_length = self.env.adjusted_length(*link)
            adjusted_length_list.append(adjusted_length)
            #required_resource = 
            #current_resource = 
            required_resource_list.append(required_resource)
            current_resource_list.append(current_resource)
            
        distance_factor = sum(adjusted_length)
        resource_factor = None###
        score = 1 / (distance_factor * resource_factor)