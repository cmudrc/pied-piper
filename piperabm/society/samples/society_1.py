from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_1 import model as model_infrastructure


model = deepcopy(model_infrastructure)
model.society.average_income = 1
agent_id = 1
home_id = model.infrastructure.homes[0]
model.society.add_agent(
    id=agent_id,
    home_id=home_id,
    socioeconomic_status=1,
    resources={
        "food": 1,
        "water": 1,
        "energy": 1,
    },
    balance=100
)


if __name__ == "__main__":
    destination_id = 2
    print(f"estimated_distance: {model.society.estimated_distance(agent_id, destination_id)} meters")
    print(f"estimated_duration: {model.society.estimated_duration(agent_id, destination_id)} seconds")
    #print(f"path: {model.society.path(agent_id, destination_id)}")
    #print(model.society.serialize())
    #model.show()