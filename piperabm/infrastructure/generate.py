import numpy as np


class Generate:
    """
    Generate infrastructure
    """
    
    def generate(
        self,
        homes_num: int = 1,
        x_grid_size: float = 1,
        y_grid_size: float = 1,
        x_num: int = 2,
        y_num: int = 2,
        imperfection_percentage: float = 0
    ):
        """
        Generate a grid world model
        """

        x_size = x_grid_size * (x_num - 1)
        y_size = y_grid_size * (y_num - 1)
        x_range = x_grid_size * x_num
        y_range = y_grid_size * y_num

        # Streets
        for i in range(x_num):
            x = (i * x_grid_size) - (x_size / 2)
            self.add_street(
                pos_1=[x, 0 - (y_size / 2)],
                pos_2=[x, y_size - (y_size / 2)]
            )
        for j in range(y_num):
            y = (j * y_grid_size) - (y_size / 2)
            self.add_street(
                pos_1=[0 - (x_size / 2), y],
                pos_2=[x_size - (x_size / 2), y]
            )

        # Market ##############
        self.add_market(
            pos=[0, 0],
            name='market',
            id=0,
            food=100,
            water=100,
            energy=100
        )

        # Homes
        def generate_random_point(x_range, y_range):
            x = np.random.uniform(-x_range/2, x_range/2)
            y = np.random.uniform(-y_range/2, y_range/2)
            pos = [x, y]
            pos = [float(num) for num in pos]  # Convert type from np.float64 to float
            return pos

        for i in range(homes_num):
            self.add_home(pos=generate_random_point(x_range, y_range))

        self.bake()

        # Random impact
        edges = self.random_edges(percent=imperfection_percentage)
        self.impact(edges=edges)


if __name__ == "__main__":

    from piperabm.infrastructure import Infrastructure

    infrastructure = Infrastructure()
    infrastructure.generate(
        homes_num=10,
        x_grid_size=15,
        y_grid_size=10,
        x_num=6,
        y_num=6
    )
    infrastructure.show()