from piperabm.infrastructure.samples.infrastructure_1 import model


model.set_seed(2)
model.society.average_income = 1
model.society.add_agent(
    id=1,
    home_id=1,
    socioeconomic_status=1,
    food=100,
    water=100,
    energy=100,
    enough_food=100,
    enough_water=100,
    enough_energy=100,
    balance=1000
)
model.set_seed(None)


if __name__ == "__main__":
    agent_id = model.society.agents[0]
    destination_id = 2
    print(f'estimated_distance: {model.society.estimated_distance(agent_id, destination_id)} meters')
    print(f'estimated_duration: {model.society.estimated_duration(agent_id, destination_id)} seconds')
    print(f'path: {model.society.path(agent_id, destination_id)}')