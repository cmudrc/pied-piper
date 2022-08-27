import matplotlib.pyplot as plt

def show_graph(x=list(), y=list(), titles=list(), node_sizes=1):
    plt.scatter(x, y, s=node_sizes, marker='o', c='#1f77b4')
    for id, title in enumerate(titles):
        plt.text(
            x[id],
            y[id] - 0.10,
            s=title,
            horizontalalignment='center',
            verticalalignment='center'
            )
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])
    plt.show()

def node_size_calculator(entity, total_source, total_demand, all_resources_names):
    summation_source = 0
    summation_demand = 0
    summation_aggregated = 0
    for resource in all_resources_names:
        summation_source += entity.source[resource] / total_source[resource]
        summation_demand += entity.demand[resource] / total_demand[resource]
        summation_aggregated += (entity.source[resource] - entity.demand[resource]) / (total_source[resource] - total_demand[resource])
    result = 10000 / (summation_demand + summation_source) ** 4
    #print(result)
    return result