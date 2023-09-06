import networkx as nx


class ToGraph:
    """
    *** Extends PathGraph Class ***
    Create graph from input
    """

    def to_graph(self, current_environment):
        """
        Create path graph from environment graph
        """

        def add_node(index):
            """
            Add node to the graph
            """
            self.G.add_node(index)

        def add_edge(index, other_index, graph):
            """
            Add edge to the graph
            """
            path = nx.shortest_path(graph.G, source=index, target=other_index, weight='adjusted_length')
            self.G.add_edge(index, other_index, path=path)

        graph = current_environment.to_active_graph()
        index_list = graph.all_indexes(type='settlement')
        #index_list += links_graph.all_nodes(type='market')
        for index in index_list:
            add_node(index)
            for other_index in index_list:
                if other_index != index and nx.has_path(self.current_environment.G, source=index, target=other_index):
                    add_edge(index, other_index, graph)