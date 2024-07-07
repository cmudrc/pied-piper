"""
Grid world
"""

import piperabm as pa


model = pa.Model(seed=2)
model.set_seed(2)
model.infrastructure.coeff_usage = 1
model.infrastructure.coeff_weather = 1
model.infrastructure.generate(
    homes_num=10,
    x_grid_size=15,
    y_grid_size=10,
    x_num=6,
    y_num=6,
    imperfection_percentage=10
)
model.set_seed(None)


if __name__ == "__main__":
    model.infrastructure.show()
