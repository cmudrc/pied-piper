from load_initial import model


print("nodes: " + str(len(model.infrastructure_nodes)))
print("edges: " + str(len(model.infrastructure_edges)))


if __name__ == "__main__":
    model.bake()