class Economy():
    def __init__(self, detailed_graph):
        self.G = detailed_graph

    def run_step(self):
        G = self.G
        for node in G.nodes:
            sources_list = G.in_edges(node)
            sorted(sources_list, key=lambda n: node[n]['source'])
            demands_list = G.out_edges(node)
            sorted(demands_list, key=lambda n: node[n]['demand'])

        def make_one_transaction(edge):
            source = node_start['source']
            source_max_discharge = node_start['max_discharge']
            source_current_discharge = node_start['current_discharge']
            demand = node_end['demand']
            demand_max_discharge = node_end['max_discharge']
            demand_current_discharge = node_end['current_discharge']
            #print(self.info[order.start]['source'], self.info[order.end]['demand'])
            if source >= demand:
                node_start['source'] = source - demand
                node_end['demand'] = 0
            else:
                node_start['source'] = 0
                node_end['demand'] = demand - source

if __name__ == "__main__":
    ''' NX '''
    import networkx as nx

    G = nx.Graph([(1, 2, {"color": "yellow"})])