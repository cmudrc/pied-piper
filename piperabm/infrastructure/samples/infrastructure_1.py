"""
Simple world
"""

import piperabm as pa


model = pa.Model()
model.infrastructure.add_street(pos_1=[0, 0], pos_2=[-60, 40], name="road")
model.infrastructure.add_home(pos=[5, 0], id=1, name='home 1')
model.infrastructure.add_home(pos=[-60, 45], id=2, name='home 2')
model.infrastructure.bake()


if __name__ == "__main__":
    model.infrastructure.show()
