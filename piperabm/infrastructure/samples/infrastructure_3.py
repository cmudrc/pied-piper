"""
Grid world without access to market
"""

import piperabm as pa


model = pa.Model(seed=2)
model.infrastructure.coeff_usage = 1
model.infrastructure.coeff_weather = 1
model.infrastructure.generate(
    homes_num=10,
    grid_size=[15, 10],
    grid_num=[6, 6],
    imperfection_percentage=10
)
model.set_seed(None)


if __name__ == "__main__":
    model.infrastructure.show()
