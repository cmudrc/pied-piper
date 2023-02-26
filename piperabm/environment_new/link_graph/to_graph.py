import networkx as nx

from piperabm.tools import ElementExists


class ToGraph:
    
    def to_graph(self, start_date=None, end_date=None):
        """
        Create path graph from environment graph
        """
        ee = ElementExists()
        def check_path_active(path, env):
            """
            Check all links within a path to see if they are all active
            """
            path_active = True
            for i, _ in enumerate(path):
                if i > 0:
                    start = path[i-1]
                    end = path[i]
                    active = env.G[start][end]['active']
                    if active is False:
                        path_active = False
                        break
            return path_active

        def calculate_path_length(path, env):
            """
            Calculate the equivalent length of path
            """
            total_length = 0
            for i, _ in enumerate(path):
                if i > 0:
                    start = path[i-1]
                    end = path[i]
                    length = env.G[start][end]['length']
                    difficulty = env.G[start][end]['difficulty']
                    #progressive_deg_coeff = env.G[start][end]['####']
                    adjusted_length = length * difficulty
                    total_length += adjusted_length
            return total_length   

        def node_exists(index, start_date, end_date):
            """
            Check whether the node has been already initiated
            """
            result = False
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
            active = None
            initiation_date = None
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

        def edge_exists(initiation_date, start_date, end_date):
            """
            Check all links within a path to see if they all exist
            """
            path_exists = True
            for i, _ in enumerate(path):
                if i > 0:
                    start = path[i-1]
                    end = path[i]
                    initiation_date = env.G[start][end]['initiation_date']
                    exists = check_existance(initiation_date, start_date, end_date)
                    if exists is False:
                        path_exists = False
                        break
            return path_exists

        env = self.env
        index_list = env.all_nodes()
        for index in index_list:
            if node_exists(index, start_date, end_date):
                add_node(index)
                for other_index in index_list:
                    if other_index != index:
                        if env.G.has_edge(index, other_index):
                            initiation_date = env.node_info(index, 'initiation_date')
                            active = env.node_info(index, 'active')
                            if edge_exists((initiation_date, start_date, end_date)) and active is True:
                                self.G.add_edge(index, other_index)
    