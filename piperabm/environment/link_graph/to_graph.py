import networkx as nx

from piperabm.tools import ElementExists


class ToGraph:
    
    def to_graph(self, start_date=None, end_date=None):
        """
        Create path graph from environment graph
        """

        ee = ElementExists()

        def node_exists(index, start_date, end_date):
            """
            Check whether the node has been already initiated
            """
            result = False
            node_type = self.env.node_type(index)
            if node_type == 'cross':
                active = True
            else:
                active = self.env.node_info(index, 'active')
            initiation_date = self.env.node_info(index, 'initiation_date')
            exists = ee.check(
                item_start=initiation_date,
                item_end=None,
                time_start=start_date,
                time_end=end_date
            )
            if exists is True and active is True:
                result = True
            return result

        def edge_exists(index, other_index, start_date, end_date):
            result = False
            active = self.env.edge_info(index, other_index, 'active')
            initiation_date = self.env.edge_info(index, other_index, 'initiation_date')
            exists = ee.check(
                item_start=initiation_date,
                item_end=None,
                time_start=start_date,
                time_end=end_date
            )
            if exists is True and active is True:
                result = True
            return result

        def add_node(index):
            name = self.env.node_info(index, 'name')
            boundary = self.env.node_info(index, 'boundary')
            pos = boundary.center
            self.G.add_node(index, name=name, pos=pos)

        def add_edge(index, other_index):
            self.G.add_edge(index, other_index)

        def refine_input(start_date, end_date):
            if end_date is None:
                if start_date is None:
                    pass
                else:
                    end_date = start_date
            return start_date, end_date

        start_date, end_date = refine_input(start_date, end_date) 
        env = self.env
        index_list = env.all_nodes()
        for index in index_list:
            if node_exists(index, start_date, end_date):
                add_node(index)
                for other_index in index_list:
                    if node_exists(other_index, start_date, end_date) and other_index != index:
                        if env.G.has_edge(index, other_index):
                            initiation_date = env.edge_info(index, other_index, 'initiation_date')
                            active = env.edge_info(index, other_index, 'active')
                            if edge_exists(index, other_index, start_date, end_date) and active is True:
                                add_edge(index, other_index)
    