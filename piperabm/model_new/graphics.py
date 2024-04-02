import matplotlib.pyplot as plt


class Graphics:

    def fig(self):
        plt.clf()
        ax = plt.gca()
        ax.set_aspect("equal")
        self.infrastructure.to_plt()
        self.society.to_plt(agents_only=True)
        return plt.gcf()
    
    def show(self):
        fig = self.fig()
        plt.show()