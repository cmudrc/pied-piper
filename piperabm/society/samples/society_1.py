from piperabm.infrastructure.samples import model_1 as model


model.society.add_agent(home_id=1, socioeconomic_status=1, id=1)
model.society.add_agent(home_id=2, socioeconomic_status=1, id=2)


if __name__ == "__main__":
    agent_id = 1
    destination_id = 2
    print(f'estimated_distance: {model.society.estimated_distance(agent_id, destination_id)} meters')
    print(f'estimated_duration: {model.society.estimated_duration(agent_id, destination_id)} seconds')
    print(f'path: {model.society.path(agent_id, destination_id)}')