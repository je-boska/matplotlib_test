import matplotlib.pyplot as plt
import numpy as np

x_values = [0, 1, 2]
y_values = [1, 4, 16]

x_log_values = [1, 4, 16]
y_log_values = [0, 1, 2]

plt.plot(x_values, y_values)
plt.plot(x_log_values, y_log_values)

plt.ylabel('y')
plt.xlabel('x')

plt.grid(b=True)
plt.xlim(0, 20)
plt.ylim(0, 20)

plt.show()
