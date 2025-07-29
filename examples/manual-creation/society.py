from infrastructure import model


# Step 2: Build the Society
# Link: https://pied-piper.readthedocs.io/latest/step-by-step.html#step-2-build-the-society
model.society.neighbor_radius = 500  # Meters
homes = model.infrastructure.homes  # Homes id
model.society.add_agent(
    home_id=homes[0],
    balance=1200,
    resources={'food': 15, 'water': 12, 'energy': 10},
)
model.society.add_agent(
    home_id=homes[1],
    balance=800,
    resources={'food': 15, 'water': 12, 'energy': 10},
)
model.society.add_agent(
    home_id=homes[1],
    balance=1100,
    resources={'food': 15, 'water': 12, 'energy': 10},
)
model.society.add_agent(
    home_id=homes[2],
    balance=900,
    resources={'food': 15, 'water': 12, 'energy': 10},
)


if __name__ == '__main__':
    print(model.society)