import matplotlib.pyplot as plt

from piperabm.graphics.animation import Animation


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

    def animate(self, output_file='output', simulation_file='simulation', framerate=15):
        animation = Animation(self.path)
        fig = self.fig()
        animation.add_figure(fig)
        # Deltas
        deltas = self.load_deltas(name=simulation_file)
        for delta in deltas:
            self.apply_delta(delta)
            fig = self.fig()
            animation.add_figure(fig)
        animation.render(output_file=output_file, framerate=framerate)
