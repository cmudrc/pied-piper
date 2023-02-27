import networkx as nx
from copy import deepcopy

from piperabm.tools import ElementExists


class ToGraph:
    """
    Create graph
    """

    def to_graph(self, start_date=None, end_date=None):
        """
        Create path graph from environment graph
        """

        ee = ElementExists()

        def node_exists(index, start_date, end_date):
            """
            Check whether the node exists between *start_date* and *end_date*
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
            """
            Check whether the edge exists between *start_date* and *end_date*
            """
            result = False
            active = self.env.edge_info(index, other_index, 'active')
            initiation_date = self.env.edge_info(
                index,
                other_index,
                'initiation_date'
            )
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
            self.G.add_edge(index, other_index)

        def refine_input(start_date, end_date):
            """
            Refine inputs
            """
            def swap(start, end):
                temp = None
                if start > end:
                    temp = deepcopy(start)
                    start = deepcopy(end)
                    end = deepcopy(temp)
                return start, end

            if end_date is None:
                if start_date is not None:
                    end_date = start_date
            return swap(start_date, end_date)

        start_date, end_date = refine_input(start_date, end_date)
        env = self.env
        index_list = env.all_nodes()
        for index in index_list:
            if node_exists(index, start_date, end_date):
                add_node(index)
                for other_index in index_list:
                    if node_exists(other_index, start_date, end_date) and other_index != index:
                        if env.G.has_edge(index, other_index):
                            if edge_exists(index, other_index, start_date, end_date):
                                add_edge(index, other_index)
        for node in self.all_nodes("cross"):
            if self.node_degree(node) == 0:
                self.G.remove_node(node)

