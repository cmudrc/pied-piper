from infrastructure import model


# Step 2: Build the Society
# Link: 
model.society.generate(
    num=50,
    gini_index=0.3,
    average_resources={'food': 10,'water': 10,'energy': 10},
    average_balance=1000,
)


if __name__ == '__main__':
    print(model.society)