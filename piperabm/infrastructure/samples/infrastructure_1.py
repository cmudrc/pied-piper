"""
Simple world with one home and one market
"""

import piperabm as pa


model = pa.Model()
model.set_seed(2)
model.infrastructure.coeff_usage = 1
model.infrastructure.coeff_weather = 1
model.infrastructure.add_street(pos_1=[0, 0], pos_2=[-60, 40], name='road')
model.infrastructure.add_home(pos=[5, 0], id=1, name='home')
model.infrastructure.add_market(
    pos=[-60, 45],
    id=2,
    name='market',
    resources={'food': 100, 'water': 100, 'energy': 100}
)
model.infrastructure.bake()
model.set_seed(None)


if __name__ == "__main__":
    model.infrastructure.show()
