import os
import piperabm as pa


path = os.path.dirname(os.path.realpath(__file__))
model = pa.Model(path=path, seed=2)

# Set up the infrastructure
model.infrastructure.add_home(pos=[0, 0], id=0, name="home")
model.infrastructure.bake()

# Set up the society
model.society.generate(num=2, gini_index=0.4, average_balance=1000)
agents = model.society.agents
# Manipulation of the agents
model.society.average_income = 0  # Set income to zero
wealth_0 = model.society.wealth(agents[0])
wealth_1 = model.society.wealth(agents[1])
if wealth_0 < wealth_1:
    id_low = agents[0]  # Agent with lower wealth
    id_high = agents[1]  # Agent with higher foowealthd
food = model.society.get_resource(id_low, "food")
model.society.set_resource(id_low, "food", value=food / 10)
water = model.society.get_resource(id_low, "water")
model.society.set_resource(id_low, "water", value=water / 5)
print(model.society)  # Print the society stat

# Compare the resources of the agents before and after the simulation
print("\n" + ">>> Initial:")
for agent in agents:
    balance = model.society.get_balance(agent)
    food = model.society.get_resource(agent, "food")
    water = model.society.get_resource(agent, "water")
    energy = model.society.get_resource(agent, "energy")
    print(
        f"id: {agent}, balance: {balance}, food: {food}, water: {water}, energy: {energy}"
    )

transactions = model.update(duration=1)

print("\n" + ">>> " + "Exchanges: ")
for transaction in transactions:
    print(
        f"from: {transaction[0]}, to: {transaction[1]}, amount: {transaction[2]}, resource: {transaction[3]}"
    )

print("\n" + ">>> Final:")
for agent in agents:
    balance = model.society.get_balance(agent)
    food = model.society.get_resource(agent, "food")
    water = model.society.get_resource(agent, "water")
    energy = model.society.get_resource(agent, "energy")
    print(
        f"id: {agent}, balance: {balance}, food: {food}, water: {water}, energy: {energy}"
    )
