import networkx as nx


class ToGraph:
    """
    *** Extends CurrentGraph Class ***
    Create graph from input
    """

    def to_graph(self, start_date=None, end_date=None):
        """
        Create current graph from environment graph
        """
        def add_node(index):
            """
            Add node to the graph
            """
            self.G.add_node(index)

        def add_edge(index, other_index, relationships):
            """
            Add edge to the graph
            """
            self.G.add_edge(index, other_index, relationships=relationships)

        def validate_agent(agent, start_date, end_date):
            """
            Is it valid to get added to the current graph?
            """
            result = False
            if agent.exists(start_date, end_date) and \
                agent.active is True:
                result = True
            return result
        
        def filter_relationships(relationships, start_date, end_date):
            filtered_relationships = {}
            for name in relationships:
                relationship = relationships[name]
                if relationship.exists(start_date, end_date):
                    filtered_relationships[name] = relationship
            return filtered_relationships

        def validate_edge(filtered_relationships, start_date, end_date):
            """
            Is it valid to get added to the current graph?
            """
            result = False
            if len(filtered_relationships) > 0:
                result = True
            return result

        def refine_input(start_date, end_date):
            """
            Refine inputs
            """
            if end_date is None:
                if start_date is not None:
                    end_date = start_date
            return start_date, end_date
            
        start_date, end_date = refine_input(start_date, end_date)
        
        ''' Filter nodes '''
        indexes = self.society.all_indexes()
        for index in indexes:
            agent = self.society.get_agent_object(index)
            valid = validate_agent(
                agent,
                start_date,
                end_date
            )
            if valid is True:
                add_node(index)

        ''' Filter edges '''
        edges = self.society.all_edges()
        for edge in edges:
            relationships = self.society.get_edge_object(*edge)
            filtered_relationships = filter_relationships(
                relationships,
                start_date,
                end_date
            )
            valid = validate_edge(
                filtered_relationships,
                start_date,
                end_date
            )
            if valid is True:
                add_edge(edge[0], edge[1], relationships=filtered_relationships)

    def to_multi_graph(self, filter='all'):
        """
        Create multi graph representation of graph for visualization pusposes
        """
        G = nx.MultiGraph()
        for index in self.all_indexes():
            G.add_node(index)
        for edge in self.all_edges():
            start_index = edge[0]
            end_index = edge[1]
            relationships = self.society.get_edge_object(start_index, end_index)
            for relationship in relationships:
                if filter == 'all' or filter == relationship:
                    #print(relationship, filter == relationship, filter)
                    G.add_edge(edge[0], edge[1], type=relationship)
        return G