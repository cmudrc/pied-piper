import networkx as nx
import matplotlib.pyplot as plt


class Graphics:
    
    def to_plt(self, ax=None):
        """
        Add elements to plt
        """
        if ax is None:
            ax = plt.gca()
        pos_dict = {}
        node_list = []
        node_size_list = []
        node_color_list = []
        label_dict = {}
        node_size = 200
        color_dict = {
            'active': 'green',
            'inactive': 'black',
        }

        for index in self.index_list:
            node = self.G.nodes[index]
            node_list.append(index)
            pos = node['pos']
            pos_dict[index] = pos
            node_size_list.append(node_size)
            label_dict[index] = node['name']
            if node['active'] == True:
                node_color_list.append(color_dict['active'])
            else:
                node_color_list.append(color_dict['inactive'])

        nx.draw_networkx(
            self.G,
            pos=pos_dict,
            nodelist=node_list,
            node_size=node_size_list,
            labels=label_dict
        )

    def show(self, start_date, end_date):
        """
        Show current state of Environment graph
        """
        self.to_plt(start_date=start_date, end_date=end_date)
        plt.show()