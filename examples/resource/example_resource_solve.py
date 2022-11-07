import matplotlib.pyplot as plt
from copy import deepcopy

from pr.asset import Resource
from pr.asset import Use, Produce, Storage, Deficiency


food = Resource(
    name='food',
    use=Use(rate=1),
    produce=Produce(rate=0.7),
    storage=Storage(current_amount=10, max_amount=20),
    deficiency=Deficiency(current_amount=5, max_amount=20)
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