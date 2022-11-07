import matplotlib.pyplot as plt

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

i = 1
while food.demand() > 0:
    plt.clf()
    plt.gca().set_title("total added: " + str(i))
    food.add(1)
    food.to_plt()
    plt.pause(interval=0.1)
    i += 1

plt.show()
