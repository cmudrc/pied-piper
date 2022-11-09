import matplotlib.pyplot as plt

import piperabm as pa


food = pa.asset.Resource(
    name='food',
    use=pa.asset.Use(rate=1),
    produce=pa.asset.Produce(rate=0.7),
    storage=pa.asset.Storage(current_amount=10, max_amount=20),
    deficiency=pa.asset.Deficiency(current_amount=5, max_amount=20)
)
food.refill(10)

i = 1
while food.demand() > 0:
    plt.clf()
    plt.gca().set_title("total added: " + str(i))
    food.add(1)
    food.to_plt()
    plt.pause(interval=0.1)
    i += 1

plt.show()
