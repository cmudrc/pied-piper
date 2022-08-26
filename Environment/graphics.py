import matplotlib.pyplot as plt

def show_graph(x=list(), y=list(), node_size=1):
    plt.scatter(x, y, s=node_size, marker='o', c='#1f77b4')
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])
    plt.show()