import matplotlib.pyplot as plt


class Graphics:
    """
    Handle graphics
    """

    def to_fig(self, ax, relationships=False):
        """
        Add model elements to plt fig ax
        """
        self.infrastructure.to_fig(ax=ax)
        self.society.to_fig(ax=ax, relationships=relationships)

    def show(self, relationships=False):
        """
        Show model elements
        """
        fig, ax = plt.subplots()
        self.to_fig(ax=ax, relationships=relationships)
        plt.show()


if __name__ == "__main__":

    from piperabm.society.samples import model_2 as model

    model.show(relationships=['neighbor'])