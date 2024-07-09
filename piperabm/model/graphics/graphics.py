import matplotlib.pyplot as plt

from piperabm.model.graphics.animation import Animation


class Graphics:
    """
    Handle graphics
    """

    def fig(
            self,
            relationships=False,
            clf=True
        ):
        """
        Add model elements to plt fig ax
        """
        if clf is True:
            plt.clf()
        ax = plt.gca()
        ax.set_aspect("equal")

        # Draw infrastructure
        fig = self.infrastructure.fig(
            clf=False
        )

        # Draw society
        fig = self.society.fig(
            relationships=relationships,
            clf=False
        )

        return fig

    def show(self, relationships=False):
        """
        Show model elements
        """
        fig = self.fig(
            relationships=relationships
        )
        plt.show()

    def animate(self):
        animation = Animation(path=self.result_directory)
        self.load_initial()

        # First frame
        fig = self.fig()
        animation.add_figure(fig)

        # Apply deltas and create frames
        deltas = self.load_deltas()
        for delta in deltas:
            self.apply_delta(delta)
            fig = self.fig()
            animation.add_figure(fig)
    
        # Render
        animation.render(output_file='animation')


if __name__ == "__main__":

    from piperabm.society.samples import model_2 as model

    model.show(relationships=['neighbor'])