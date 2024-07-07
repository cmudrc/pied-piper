"""
A single home standing in the middle of nowhere
"""

import piperabm as pa


model = pa.Model()
model.set_seed(2)
model.infrastructure.coeff_usage = 1
model.infrastructure.coeff_weather = 1
model.infrastructure.add_home(pos=[0, 0], id=0, name='home')
model.infrastructure.bake()
model.set_seed(None)


if __name__ == "__main__":
    model.infrastructure.show()
