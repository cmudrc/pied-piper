import matplotlib.pyplot as plt
from copy import deepcopy

import piperabm as pa


food = pa.asset.Resource(
    name='food',
    use=pa.asset.Use(rate=1),
    produce=pa.asset.Produce(rate=0.7),
    storage=pa.asset.Storage(current_amount=10, max_amount=20),
    deficiency=pa.asset.Deficiency(current_amount=5, max_amount=20)
)
food.refill(10)

interval = 0.7
for _ in range(100):
    plt.clf()
    plt.gca().set_title("before")
    food.to_plt()
    plt.pause(interval)

    plt.clf()
    plt.gca().set_title("after")
    food_after = deepcopy(food)
    food_after.solve()
    food_after.to_plt()
    plt.pause(interval)

plt.show()