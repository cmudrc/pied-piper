import networkx as nx

try: from .path import Path
except: from path import Path


class ToGraph:

    def to_graph(self, links_graph):
        """
        Create path graph from environment graph
        """

        def add_node(index):
            """
            Add node to the graph
            """
            name = self.env.node_info(index, 'name')
            boundary = self.env.node_info(index, 'boundary')
            pos = boundary.center
            self.G.add_node(index, name=name, pos=pos)

        def add_edge(index, other_index):
            """
            Add edge to the graph
            """
            path = nx.shortest_path(self.env.G, source=index, target=other_index)
            r = Path(path, self.env)
            #print(r)
            self.G.add_edge(index, other_index, path=r)
            #length = self.calculate_path_length(path)
            #self.G.add_edge(index, other_index, path=path, length=length)
            
                    

        index_list = links_graph.all_nodes(type='settlement')
        index_list += links_graph.all_nodes(type='market')
        for index in index_list:
            add_node(index)
            for other_index in index_list:
                if other_index != index and nx.has_path(self.env.G, source=index, target=other_index):
                    add_edge(index, other_index)
