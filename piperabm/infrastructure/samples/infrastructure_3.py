"""
Grid world
"""

import random

import piperabm as pa


""" Info """
homes_num = 10
x_grid_size = 15
y_grid_size = 10
x_num = 6
y_num = 6
x_size = x_grid_size * (x_num - 1)
y_size = y_grid_size * (y_num - 1)
x_range = x_grid_size * x_num
y_range = y_grid_size * y_num
imperfection_percentage = 10


""" Model """
model = pa.Model()

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

edges = model.infrastructure.random_edges(percent=imperfection_percentage)
model.infrastructure.impact(edges=edges)


if __name__ == "__main__":
    #print(model.infrastructure.serialize())
    model.infrastructure.show()
