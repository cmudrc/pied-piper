def utility(x, critical=0):
    if x < critical:
        slope = 1 / critical
        y = slope * x
    else:
        y = 1
    return y


if __name__ == "__main__":

    import numpy as np
    from matplotlib import pyplot as plt

    critical = 1

    xs = np.linspace(
        start=0,
        stop=2*critical,
        num=100
    )
    ys = [utility(x, critical) for x in xs]

    plt.xlabel('x')
    plt.ylabel('Utility')
    plt.title('Utility Function')
    plt.plot(xs, ys)
    plt.grid(True)
    plt.show()
