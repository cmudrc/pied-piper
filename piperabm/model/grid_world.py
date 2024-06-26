import random

from piperabm.model import Model


def grid_world(
    name: str = 'model',
    path = None,
    homes_num: int = 1,
    x_grid_size: float = 1,
    y_grid_size: float = 1,
    x_num: int = 1,
    y_num: int = 1,
    imperfection_percentage = 10,
    seed: int = None
):
    """
    Create a grid world model
    """
    
    random.seed(seed)
    
    x_size = x_grid_size * (x_num - 1)
    y_size = y_grid_size * (y_num - 1)
    x_range = x_grid_size * x_num
    y_range = y_grid_size * y_num

    model = Model(name=name, path=path)

    # Streets
    for i in range(x_num):
        x = (i * x_grid_size) - (x_size / 2)
        model.infrastructure.add_street(
            pos_1=[x, 0 - (y_size / 2)],
            pos_2=[x, y_size - (y_size / 2)]
        )
    for j in range(y_num):
        y = (j * y_grid_size) - (y_size / 2)
        model.infrastructure.add_street(
            pos_1=[0 - (x_size / 2), y],
            pos_2=[x_size - (x_size / 2), y]
        )

    # Market
    model.infrastructure.add_market(
        pos=[0, 0],
        name='market',
        id=0,
        food=100,
        water=100,
        energy=100
    )

    # Homes
    def generate_random_point(x_range, y_range):
        x = random.uniform(-x_range/2, x_range/2)
        y = random.uniform(-y_range/2, y_range/2)
        pos = [x, y]
        pos = [float(num) for num in pos]  # Convert type from np.float64 to float
        return pos
    
    for i in range(homes_num):
        model.infrastructure.add_home(pos=generate_random_point(x_range, y_range))


    model.infrastructure.bake()  

    # Random impact
    edges = model.infrastructure.random_edges(percent=imperfection_percentage)
    model.infrastructure.impact(edges=edges)  

    random.seed(None)

    return model


if __name__ == "__main__":
    model = grid_world(
        homes_num=10,
        x_grid_size=15,
        y_grid_size=10,
        x_num=6,
        y_num=6,
        imperfection_percentage=10,
        seed=1
    )
    model.show()