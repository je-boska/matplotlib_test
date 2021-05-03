import matplotlib.pyplot as plt
import numpy as np

point1 = (0, 10)
point2 = (10, 30)

x_values = (point1[0], point2[0])
y_values = (point1[1], point2[1])

plt.plot(x_values, y_values, 'bo-')

plt.ylabel('y')
plt.xlabel('x')
plt.show()
