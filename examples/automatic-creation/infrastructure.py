import os
import piperabm as pa


# Step 0: Create the Model
# Link: 
model = pa.Model(
    path=os.path.dirname(os.path.realpath(__file__)),
    seed=10
)

# Step 1: Build the Infrastructure
# Link: 
model.infrastructure.generate(
    homes_num=20,
    grid_size=[15, 10],  # Meters
    grid_num=[6, 6],  # Meters
    imperfection_percentage=10  # Percentage of imperfection in the grid
)
model.infrastructure.add_market(
    pos=[0, 0],
    name='market',
    id=0,
    resources={'food': 150, 'water': 220, 'energy': 130}
)
model.bake()


if __name__ == '__main__':
    print(model.infrastructure)
    model.infrastructure.show()