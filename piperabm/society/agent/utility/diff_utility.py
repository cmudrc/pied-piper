from piperabm.tools.symbols import SYMBOLS


def diff_utility(x, x_critical=SYMBOLS['eps'], y_max=1):
    diff_y = None
    if x < x_critical:
        diff_y = y_max / x_critical
    else:
        diff_y = 0
    return diff_y


if __name__ == "__main__":

    import numpy as np
    from matplotlib import pyplot as plt

    x_critical = 1
    y_max = 1

    xs = np.linspace(start=0, stop=2*x_critical, num=100)
    ydiffs = [diff_utility(x, x_critical, y_max) for x in xs]

    plt.xlabel('x')
    plt.ylabel('Diff Utility')
    plt.title('Diff Utility Function')
    plt.plot(xs, ydiffs)
    plt.grid(True)
    plt.show()
