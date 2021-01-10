import numpy as np
import matplotlib.pyplot as plt

def example_making_graph():
    y = 200 + np.random.randn(100)
    x = range(len(y))
    plt.plot(x, y)
    plt.title("First Picture")
    plt.show()

example_making_graph()

from numpy import exp, pi, sqrt

def gaussian(x, mu: float=0.0, sigma: float=sqrt(0.19)) -> int:
    """Calculate a value of Gaussian function"""
    gaus_val = (1/sqrt(2*pi*sigma**2))*exp(-((x-mu)**2)/2*sigma**2)
    return gaus_val

def plot_gaussian():
    x = np.arange(100)
    x = np.concatenate((-1*x[1:][::-1], x), axis=0)
    print(f"X : {x}")
    y = gaussian(x)
    print(type(y))
    print(f"Y : {y}")
    plt.plot(x, y)
    plt.title("Gaussian plot")
    plt.show()


try:
    plot_gaussian()
except BaseException as err:
    print(err)

a = input()