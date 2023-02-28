import matplotlib.pyplot as plt
#import networkx as nx


class Graphics:
    """
    Contains methods for Environment class
    """

    def to_plt(self, ax=None):
        """
        Add elements to plt
        """
        if ax is None:
            ax = plt.gca()
        start_date = self.current_date - self.step_size
        end_date = self.current_date
        args = (ax, start_date, end_date)
        self.env.to_plt(*args)
        self.society.to_plt(ax)
    
    def show(self):
        self.to_plt()
        plt.gca().set_title(self.current_date)
        plt.show()