import matplotlib.pyplot as plt
import numpy as np


def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, "--")


abline(3, 5)
plt.show()
