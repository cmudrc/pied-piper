import matplotlib.pyplot as plt


class Graphics:
    """
    Contains methods for Environment class
    Add graphical functionality
    """

    def to_plt(self, start_date=None, end_date=None, ax=None):
        link_graph = self.to_link_graph(start_date, end_date)
        link_graph.to_plt()

    def show(self, start_date, end_date, graph='links'):
        """
        Show current state of Environment graph
        """
        if graph == 'links':
            self.to_plt(start_date, end_date)
            plt.show()
        else:
            path_graph = self.to_path_graph(start_date, end_date)
            path_graph.show()
