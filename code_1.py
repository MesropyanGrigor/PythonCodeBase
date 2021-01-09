import numpy as np
import matplotlib.pyplot as plt

def example_making_graph():
    y = 200 + np.random.randn(100)
    x = range(len(y))
    plt.plot(x, y)
    plt.title("First Picture")
    plt.show()


example_making_graph()