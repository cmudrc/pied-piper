from piperabm.tools.symbols import SYMBOLS


def utility(x, x_critical=SYMBOLS['eps'], y_max=1):
    y = None
    if x < x_critical:
        slope = y_max / x_critical
        y = slope * x
    else:
        y = y_max
    return y


if __name__ == "__main__":

    import numpy as np
    from matplotlib import pyplot as plt

    x_critical = 1
    y_max = 1

    xs = np.linspace(start=0, stop=2*x_critical, num=100)
    ys = [utility(x, x_critical, y_max) for x in xs]

    plt.xlabel('x')
    plt.ylabel('Utility')
    plt.title('Utility Function')
    plt.plot(xs, ys)
    plt.grid(True)
    plt.show()
