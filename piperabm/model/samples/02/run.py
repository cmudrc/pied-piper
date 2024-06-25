import os

from piperabm.infrastructure.samples import model_1 as model


model.path = os.path.dirname(os.path.realpath(__file__))
model.society.generate_agents(
    num=10,
    average_balance=100
)
agents = model.society.agents
nonjunctions = model.infrastructure.nonjunctions
#print(model.society.estimated_duration(agent_id=agents[0], destination_id=markets[0]))
#model.save_initial()
#for agent in agents:
#    for node in nonjunctions:
#        model.society.estimated_distance(agent, node)
#print(nonjunctions)
#print(model.society.estimated_distance(agents[0], 0))
print(model.infrastructure.heuristic_paths.serialize())
#model.run(n=1, save=False, report=True, step_size=1)
#print(model.society.serialize())