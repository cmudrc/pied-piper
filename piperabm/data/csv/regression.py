import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


""" Functions """

def linear_model(x, a, b):
    return a * x + b

def poly2nd(x, a, b, c):
    """
    2nd order
    """
    return a * x**2 + b * x + c

def poly3rd(x, a, b, c, d):
    """
    3rd order
    """
    return a * x**3 + b * x**2 + c * x + d

def poly4th(x, a, b, c, d, e):
    """
    3rd order
    """
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

def exponential(x, a, b):
    """
    Exponential
    """
    #return a * b**x
    return a * np.exp(b * x)


""" Fit """

def fit(x, y, function):
    """
    Fit
    """
    coefficients, pcov = curve_fit(function, x, y)
    return coefficients

def predict(x, function, coefficients):
    """
    Predict
    """
    return function(x, *coefficients)

def rmse(y, y_predicted):
    """
    Rooted mean square error
    """
    return np.sqrt(np.mean((y - y_predicted)**2))

def goodness(x, y, function, coefficients):
    """
    Goodness of fit
    """
    y_predicted = function(np.array(x), *coefficients)
    return rmse(y=y, y_predicted=y_predicted)

def show(x, y, function, coefficients, x_label: str = 'x', y_label: str = 'y', title: str = ''):
    """
    Show the data and prediction
    """
    #print(min(x), max(x))
    x_predicted = np.linspace(start=min(x), stop=max(x), num=100)
    y_predicted = function(x_predicted, *coefficients)
    #plt.figure(figsize=(10, 6))
    plt.plot(x_predicted, y_predicted, label='Fitted Model', color='blue')
    plt.scatter(x, y, color='red', label='Actual Data')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    #plt.grid(True)
    plt.show()

def remove_none_values(x, y):
    """
    Remove entries where the temperature is None.
    """
    #valid_indices = [i for i, _ in enumerate(x) if i is not None]
    valid_indices = [i for i, val in enumerate(y) if val is not None]
    valid_x = [x[i] for i in valid_indices]
    valid_y = [y[i] for i in valid_indices]
    return valid_x, valid_y


if __name__ == "__main__":
    # Barrow 1 (N. Meadow Lake No.1 / NML-1)
    # Borehole Data
    # Date: 8/22/14

    '''
    # Without Nones
    depths = [10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 44.9]
    temperatures = [-5.636, -7.369,	-7.512,	-7.642,	-7.805,	-7.972,	-8.2, -8.415, -8.566, -8.749, -8.934, -9.069, -9.137, -9.204, -9.272, -9.34, -9.408, -9.442, -9.477, -9.511]
    '''
    # With Nones
    depths = [2, 4, 6, 8, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 44.9, 45.04]
    temperatures = [None, None, None, None, -5.636, -7.369,	-7.512,	-7.642,	-7.805,	-7.972,	-8.2, -8.415, -8.566, -8.749, -8.934, -9.069, -9.137, -9.204, -9.272, -9.34, -9.408, -9.442, -9.477, -9.511, None]

    depths, temperatures = remove_none_values(x=depths, y=temperatures)

    #function = linear_model
    function = poly2nd
    #function = poly3rd
    #function = poly4th
    #function = exponential

    coefficients = fit(x=depths, y=temperatures, function=function)
    temperature_0 = predict(x=0, function=function, coefficients=coefficients)
    print("surface temperature: ", temperature_0)
    print("goodness of fit: ", goodness(x=depths, y=temperatures, function=function, coefficients=coefficients))
    show(x=depths, y=temperatures, function=function, coefficients=coefficients)
