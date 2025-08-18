"""
.. module:: piperabm.infrastructure.generate
:synopsis: Generate infrastructure based on gridworld map.
"""

import numpy as np


class Generate:
    """
    Generate infrastructure
    """

    def generate(
        self,
        homes_num: int = 1,
        grid_size: list = [1, 1],
        grid_num: list = [2, 2],
        imperfection_percentage: float = 0,
    ):
        """
        Generate a grid world model.

        Parameters
        ----------
        homes_num : int
            Number of homes to be generated.
        grid_size : list
            Size of the grid in meters provided as list of two numbers showing the width and height of the grid.
        grid_num : list
            Number of grid cells in the provided as a list of two integers showing number of cells in the width and height of the world.
        imperfection_percentage : float, optional
            Percetnage of random imperfections in the world. This is used to create a more realistic world by introducing some randomness in the grid structure. The percentage is calculated based on the length of the removed edges. The default is 0%.
        """

        x_size = grid_size[0] * (grid_num[0] - 1)
        y_size = grid_size[1] * (grid_num[1] - 1)
        x_range = grid_size[0] * grid_num[0]
        y_range = grid_size[1] * grid_num[1]

        # Streets
        for i in range(grid_num[0]):
            x = (i * grid_size[0]) - (x_size / 2)
            self.add_street(
                pos_1=[x, 0 - (y_size / 2)], pos_2=[x, y_size - (y_size / 2)]
            )
        for j in range(grid_num[1]):
            y = (j * grid_size[1]) - (y_size / 2)
            self.add_street(
                pos_1=[0 - (x_size / 2), y], pos_2=[x_size - (x_size / 2), y]
            )

        self.bake()

        # Random impact
        edges = self.random_edges(percent=imperfection_percentage)
        self.impact(edges=edges)

        # Homes
        def generate_random_point(x_range, y_range):
            x = float(np.random.uniform(-x_range / 2, x_range / 2))
            y = float(np.random.uniform(-y_range / 2, y_range / 2))
            pos = [x, y]
            # pos = [float(num) for num in pos]  # Convert type from np.float64 to float
            return pos

        for i in range(homes_num):
            self.add_home(pos=generate_random_point(x_range, y_range))


if __name__ == "__main__":

    from piperabm.infrastructure import Infrastructure

    infrastructure = Infrastructure()
    infrastructure.generate(
        homes_num=10,
        grid_size=[15, 10],
        grid_num=[6, 6],
    )
    infrastructure.show()
